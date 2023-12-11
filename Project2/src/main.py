from interface import Assignment, CSP, Variable
from typing import Optional
from iotools import IOTools

def isComplete(assignment: Assignment) -> bool:
  pass

def getUnassignedVariable(assignment: Assignment) -> Variable:
  pass

def isConsistent() -> bool:
  pass

def solveCSP(CSP: CSP) -> Assignment:
  assignment: Assignment = {}
  def backtrack() -> Optional[Assignment]:
    if isComplete(assignment):
      return assignment
    variable = getUnassignedVariable(assignment)
    for value in CSP.domains[variable]:
      if isConsistent(variable, value):
        assignment[variable] = value
        result = backtrack()
        if result is not None:
          return result
        del assignment[variable]
    return None
  return assignment

def main():
  io = IOTools()
  CSP = io.readCSP()
  answer = solveCSP(CSP)
  io.writeAnswer(answer)

if __name__ == "__main__":
    main()