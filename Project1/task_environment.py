from typing import List, Tuple
from interface import Cube

class TaskEnvironment:
  def __init__(self, init_state: Cube, goal_state: Cube):
    self.init_state = init_state
    self.cur_state = init_state
    self.goal_state = goal_state

  def calculateHeuristic(self, state: Cube) -> int:
    # use state and self.goal_state
    # TODO
    return 0
  
  def isGoal(self, state: Cube) -> bool:
    return self.calculateHeuristic(state) == 0
