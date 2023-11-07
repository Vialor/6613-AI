from typing import List, Tuple

Position = Tuple[int, int, int] # [(x, y, z)]
Cube = List[Position] # num -> position, length 27
CUBE_LENGTH = 27
DIRECTION = {
  'UP': (0, 0, -1),
  'DOWN': (0, 0, 1),
  'NORTH': (0, -1, 0),
  'SOUTH': (0, 1, 0),
  'WEST': (-1, 0, 0),
  'EAST': (1, 0, 0)
}