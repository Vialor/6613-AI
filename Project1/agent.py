import heapq
from typing import List
from interface import DIRECTION, Cube


class Agent:
  def __init__(self, task_environment):
    self.node_history = {} # Cube: minmum total cost (g not f), parent Cube, last move direction
    self.task_environment = task_environment
    self.node_count = 0
    self.frontier = [(0, task_environment.init_state)] # priority queue: (f=g+h, Cube)

  def act(self,curState: Cube, direction) -> Cube:
    # if state has been visited # Maybe check against node_history? also check if move is valid
    ## return None
    # else
    ## calculate child by exchanging elems in curState
    # return child
    tmp_list=[]
    for pos in curState[0]:
      for dir in direction:
        if pos + dir > 2 or pos + dir < 0:
          pass
        else:
          tmp_list.append(pos+dir)
    tmp_tuple = tuple(tmp_list)
    try:
      index = curState.index(tmp_tuple)
      tmp_tuple2 = curState[index]
      curState[index] = curState[0]
      curState[0] = tmp_tuple2
    except ValueError:
      print(f"{tmp_tuple} is not in the list.")

    if curState in self.node_history:
      pass
    return curState
  
  def expand(self, direction: int) -> List[Cube]:
    children = []
    for direction in DIRECTION.keys():
      child = self.act(self.task_environment.curState, direction)
      if child is not None:
        children.append(child)
    return children

  def popFrontier(self):
    return heapq.pop(self.frontier)

  def pushFrontier(self, newNode: Cube, parentCost: int):
    fValue = self.task_environment.calculateHeuristic(newNode) + parentCost
    heapq.push(self.frontier, (fValue, newNode))
  
  def generateSolutions(self):
    # self.task_environment.goal_state, self.node_history
    return ''

  def output(self, path):
    f = open(path, "w")
    f.write(self.task_environment.input_file + '\n\n')
    f.write(self.generateSolutions())
    f.close()
