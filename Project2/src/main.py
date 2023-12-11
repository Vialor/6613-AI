from interface import Assignment, CSP, Variable, Variables, Constraints
from typing import Optional
from iotools import IOTools



def main():
  def isComplete() -> bool:
    nonlocal CSP
    return all[[v.value != -1 for v in CSP[0]]]

  def getUnassignedVariable(assignment: Assignment) -> Variable:
    # MRV
    # v in variables
    # check v.domain
    # produce potentialVars
    
    # degree heuristic
    # for v in potentialVars
    # check number of neighbors
    pass

  def isConsistent(variable: Variable) -> bool:
    for constraint in variable.constraints:
      if not constraint.evaluate():
        return False
    return True
  
  def solveCSP() -> bool:
    nonlocal CSP
    variables = CSP[0]
  
    def backtrack() -> bool:
      if isComplete(variables):
        return True
      variable = getUnassignedVariable()
      for v in variable.domain:
        variable.value = v
        if isConsistent(variable):
          if backtrack():
            return True
        variable.value = -1
      return False
    
  io = IOTools()
  CSP = io.readCSP()
  success = solveCSP()
  if success:
    io.writeAnswer(CSP[0])
  else:
    print("No solution.")

if __name__ == "__main__":
  main()