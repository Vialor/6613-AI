from interface import Variable
from iotools import IOTools
import sys

INPUT_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]


def main():
  def isComplete() -> bool:
    nonlocal CSP
    return all([var.value != -1 for var in CSP[0].values()])

  def getUnassignedVariable() -> Variable:
    nonlocal CSP
    variables = CSP[0]

    ## MRV
    potentialVars, minMRV = [], float("inf")
    for v in variables.values():
      if v.value != -1:
        continue
      # calculate MRV
      MRV = len(v.domain)
      for usedValue in variables.values():
        if usedValue in v.domain:
          MRV -= 1
      # update potentialVars
      if MRV == minMRV:
        potentialVars.append(v)
      elif MRV < minMRV:
        minMRV = len(v.domain)
        potentialVars = [v]
    if len(potentialVars) == 1:
      return potentialVars[0]
    
    ## Degree heuristic
    minDegreeVar, minNeighborCount = None, float("inf")
    for var in potentialVars:
      neighbors = set()
      for c in var.constraints:
        for neighbor in c.variables:
          if neighbor.value == -1:
            neighbors.add(neighbor)
      if minNeighborCount > len(neighbors):
        minNeighborCount = len(neighbors)
        minDegreeVar = var
    return minDegreeVar

  def isConsistent(variable: Variable) -> bool:
    return all([constraint.evaluate(*constraint.variables) for constraint in variable.constraints])
  
  def solveCSP() -> bool:
    def backtrack() -> bool:
      if isComplete():
        return True
      variable = getUnassignedVariable()
      for v in variable.domain:
        variable.value = v
        if isConsistent(variable) and backtrack():
          return True
        variable.value = -1
      return False

    return backtrack()
    
  io = IOTools()
  CSP = io.readCSP(INPUT_PATH)
  if solveCSP():
    io.writeAnswer(CSP[0], OUTPUT_PATH)
  else:
    print("No solution.")

if __name__ == "__main__":
  main()