from typing import List, Tuple

Cube = List[Tuple[int]]
DIRECTION = {
  'UP': (0, 0, -1),
  'DOWN': (0, 0, 1),
  'NORTH': (0, -1, 0),
  'SOUTH': (0, 1, 0),
  'WEST': (-1, 0, 0),
  'EAST': (1, 0, 0)
}