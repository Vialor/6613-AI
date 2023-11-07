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
    inputFile = f.read()
    nums = inputFile.split()
    for i, num in enumerate(nums[:CUBE_LENGTH]):
      init_state[int(num)] = self.orderToPosition(i)
    for i, num in enumerate(nums[CUBE_LENGTH:]):
      goal_state[int(num)] = self.orderToPosition(i)
    return init_state, goal_state

  def calculateOptimalPath():
    pass

  def output(goal_state, node_history: dict):
    # copy from self.inputFile
    # calculateOptimalPath
    node_history[goal_state] # minmum total cost (g not f), parent Cube, last move direction
    # Line 26 is the total number of nodes N generated in your tree (including the root node.) 

    # Line 27 contains the solution (a sequence of actions from root node to goal node) represented by A’s. The A’s are separated by blank spaces. Each A is a character from the set {E, W, N, S, U, D}, representing the East, West, North, South, Up and Down movements of the blank position. 

    # Line 28 contains the f(n) values of the nodes along the solution path, from the root node to the goal node, separated by blank spaces. There should be d number of A values in line 27 and d+1 number of f values in line 28.
    pass