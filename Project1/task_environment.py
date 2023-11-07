from typing import List, Tuple
from interface import CUBE_LENGTH, Cube, Position

class TaskEnvironment:
  def __init__(self, init_state: Cube, goal_state: Cube):
    self.init_state = init_state
    self.cur_state = init_state
    self.goal_state = goal_state
  
  def manhattan_distance(self, pos1: Position, pos2: Position):
    distance = 0
    for i in range(len(pos1)):
      distance += abs(pos1[i] - pos2[i])
    print(distance)
    return distance

  def calculateHeuristic(self, state: Cube) -> int:
    heuristic = 0
    # use state and self.goal_state
    for i in range(1, CUBE_LENGTH):
      heuristic += self.manhattan_distance(state[i], self.goal_state[i])
    return heuristic
  
  def isGoal(self, state: Cube) -> bool:
    return self.calculateHeuristic(state) == 0
