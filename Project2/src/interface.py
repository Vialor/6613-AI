from typing import List, Dict
Variable = str
Variables = List[Variable]
Domains = Dict[Variable, List[int]] # List[int] should be sorted
Constraints = List[any]
CSP = Dict["variables": Variables,
  "domains": Domains,
  "constraints": Constraints]
Assignment = List[Variable: int]