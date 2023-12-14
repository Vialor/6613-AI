from interface import CSP, Variable, Variables, Constraints
from typing import Optional
from iotools import IOTools


def main():
  def isComplete() -> bool:
    nonlocal CSP
    return all[[v.value != -1 for v in CSP[0]]]

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