from testHelper import printVars
from interface import CSP, Variable, Variables, Constraints
from typing import Optional
from iotools import IOTools

INPUT_PATH = "../test/Input1.txt"
OUTPUT_PATH = "../test/Putput1.txt"


def main():
  def isComplete() -> bool:
    nonlocal CSP
    return all([var.value != -1 for var in CSP[0].values()])

  def getUnassignedVariable() -> Variable:
    nonlocal CSP
    variables = CSP[0]

    # MRV
    # v in variables
    # check v.domain
    # produce potentialVars

    count = 0
    min = 99
    MRV_list = []
    for v in variables.values():
      if v.value!=-1:
        count+=1
    for v in variables.values():
      v.MRV = len(v.domain)-count
      if v.MRV<min:
        min = v.MRV
    for v in variables.values():
      if v.value != -1 and v.MRV == min:
        MRV_list.append(v.name)

    # degree heuristic
    # for v in potentialVars
    # check number of neighbors
    for key in MRV_list:
      v = variables[key]
      v.degree = 0
      for constraint in v.constraints:
        v.degree += len(constraint.variables)-1

    min_degree_var = None
    min_degree = 99
    for v in variables.values():
      if min_degree > v.degree:
        min_degree_var = v
        min_degree = v.degree

    return min_degree_var

  def isConsistent(variable: Variable) -> bool:
    return all([constraint.evaluate(*constraint.variables) for constraint in variable.constraints])
  
  def solveCSP() -> bool:
    nonlocal CSP
    variables = CSP[0]
  
    def backtrack() -> bool:
      # printVars(variables)
      if isComplete():
        return True
      variable = getUnassignedVariable()
      print(variable.name)
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