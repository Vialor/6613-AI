import heapq
from typing import List, Optional
from interface import DIRECTION, Cube, Position


class Agent:
  def __init__(self, task_environment):
    self.task_environment = task_environment
    # keys: Cube state
    # values: [g value, h value, parent Cube, last move direction]
    self.node_history = {
      hash(tuple(task_environment.init_state)): [0, task_environment.calculateHeuristic(task_environment.init_state), None, None]
    }
    self.node_count = 0
    self.frontier = [(0, task_environment.init_state)] # priority queue: (f=g+h, Cube)

  ## FUNCTIONS TO EXPAND NODES ##
  def act(self, cur_state: Cube, direction: str) -> Optional[Cube]:
    cur_state = cur_state[:]
    parent_hash = hash(tuple(cur_state))
    offsets = DIRECTION[direction]
    tmp_tuple = tuple((cur_state[0][i] + offsets[i] for i in range(len(offsets))))
    if any([e > 2 or e < 0 for e in tmp_tuple]):
      return None
    index = cur_state.index(tmp_tuple)
    cur_state[index], cur_state[0] = cur_state[0], cur_state[index]
    if hash(tuple(cur_state)) in self.node_history.keys():
      return None
    self.node_count += 1
    self.gValue = self.node_history[parent_hash][0] + 1
    self.node_history[hash(tuple(cur_state))] = [self.gValue, self.task_environment.calculateHeuristic(cur_state), parent_hash, direction]

    return cur_state

  def expand(self, node):
    children = []
    for direction in DIRECTION.keys():
      child = self.act(node, direction)
      if child is not None:
        children.append(child)
    return children

  ## FRONTIER MANIPULATION
  def popFrontier(self) -> (int, Cube):
    return heapq.heappop(self.frontier)

  def pushFrontier(self, newNode: Cube):
    record = self.node_history[hash(tuple(newNode))]
    heapq.heappush(self.frontier, (record[0] + record[1], newNode))

  ## OUTPUT HANDLERS ##
  # calculate for the best solution: the number of steps, total nodes expnded, actions and f values along the path
  def generateSolutions(self):
    solution_fValues, solution_actions = [], []
    cur_hash = hash(tuple(self.task_environment.goal_state))
    root_hash = hash(tuple(self.task_environment.init_state))
    while cur_hash != root_hash:
      gValue, hValue, cur_hash, last_move = self.node_history[cur_hash]
      solution_actions.append(last_move[0])
      solution_fValues.append(str(gValue + hValue))
    hValue = self.node_history[root_hash][1]
    solution_fValues.append(str(hValue))
    output = []
    output.append(str(len(solution_actions)))
    output.append(str(self.node_count))
    output.append(' '.join(solution_actions[::-1]))
    output.append(' '.join(solution_fValues[::-1]))
    return '\n'.join(output)

  # write the result to a file
  def output(self, path):
    f = open(path, "w")
    f.write(self.task_environment.input_file + '\n\n')
    f.write(self.generateSolutions())
    f.close()
