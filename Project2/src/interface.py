from typing import List, Dict, Tuple, Callable

Domain = List[int] # List[int] should be sorted

class Variable:
  def __init__(self, name: str, domain: Domain):
    self.name: str = name
    self.domain: Domain = domain
    self.constraints: Constraints = []
    self.value = -1
    
ConstraintFunction = Callable[[Dict[str, Variable]], bool]

class Constraint:
  def __init__(self, variables, evaluate):
    self.variables: List[Variable] = variables
    self.evaluate: ConstraintFunction = evaluate

Variables = Dict[str, Variable]
Constraints = List[Constraint]
CSP = Tuple[Variables, Constraints]
