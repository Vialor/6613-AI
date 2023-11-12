from typing import List, Tuple
from interface import CUBE_LENGTH, Cube, Position

class TaskEnvironment:
  def __init__(self, path):
    f = open(path, "r")
    self.input_file = f.read()
    f.close()

    self.init_state, self.goal_state = self.deserialize(self.input_file)

  # order = x + 3y + 9z
  def orderToPosition(self, order: int) -> Tuple[int, int, int]:
    x = order % 3
    order //= 3
    y = order % 3
    order //= 3
    z = order % 3
    return (x, y, z)

  def deserialize(self, input_file: str) -> tuple[Cube, Cube]:
    init_state = [-1] * 27
    goal_state = [-1] * 27
    nums = input_file.split()
    for i, num in enumerate(nums[:CUBE_LENGTH]):
      init_state[int(num)] = self.orderToPosition(i)
    for i, num in enumerate(nums[CUBE_LENGTH:]):
      goal_state[int(num)] = self.orderToPosition(i)
    return init_state, goal_state
  
  def manhattan_distance(self, pos1: Position, pos2: Position):
    distance = 0
    for i in range(len(pos1)):
      distance += abs(pos1[i] - pos2[i])
    return distance

  def calculateHeuristic(self, state: Cube) -> int:
    heuristic = 0
    for i in range(1, CUBE_LENGTH):
      heuristic += self.manhattan_distance(state[i], self.goal_state[i])
    return heuristic
  
  def isGoal(self, state: Cube) -> bool:
    return self.calculateHeuristic(state) == 0
