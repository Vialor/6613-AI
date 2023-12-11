from typing import List, Dict, Tuple, Callable
from constraintHypergraph import Variable

class Variable:
  def __init__(self, name: str):
    self.name = name
    self.value = -1
    self.domain: Domain = []
    self.constraints: Constraints = []

class Constraint:
  def __init__(self):
    self.variables: Variables = []
    self.evaluate: ConstraintFunction = lambda : True

Domain = List[int] # List[int] should be sorted
ConstraintFunction = Callable[[], bool]
Variables = Dict[str, Variable]
Constraints = List[Constraint]
CSP = Tuple[Variables, Constraints]
