from typing import List, Tuple

from interface import CUBE_LENGTH, Cube

class Serialization:
  # order = x + 3y + 9z
  def orderToPosition(self, order: int) -> Tuple[int, int, int]:
    x = order % 3
    order //= 3
    y = order % 3
    order //= 3
    z = order % 3
    return (x, y, z)

  def deserialize(self, path: str) -> tuple[Cube, Cube]:
    f = open(path, "r")
    init_state = [-1] * 27
    goal_state = [-1] * 27
    nums = f.read().split()
    for i, num in enumerate(nums[:CUBE_LENGTH]):
      init_state[int(num)] = self.orderToPosition(i)
    for i, num in enumerate(nums[CUBE_LENGTH:]):
      goal_state[int(num)] = self.orderToPosition(i)
    return init_state, goal_state

  def calculateOptimalPath():
    pass

  def serialize():
    # calculateOptimalPath
    pass