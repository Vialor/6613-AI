import heapq
from typing import List
from interface import DIRECTION, Cube


class Agent:
  def __init__(self, task_environment):
    self.nodeHistory = {} # Cube: minmum total cost (g not f), parent Cube, last move direction
    self.taskEnvironment = task_environment
    self.nodeCount = 0
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

    if curState in self.nodeHistory:
      pass
    return curState
  
  def expand(self, direction: int) -> List[Cube]:
    children = []
    for direction, move in DIRECTION.items():
      child = self.act(self.task_environment.curState, direction)
      if child is not None:
        children.append(child)
    return children

  def popFrontier(self):
    return heapq.pop(self.frontier)

  def pushFrontier(self, newNode: Cube, parentCost: int):
    fValue = self.taskEnvironment.calculateHeuristic(newNode) + parentCost
    heapq.push(self.frontier, (fValue, newNode))
    