from constraintFunction import allDiffConstraint, generateAdditionConstraint
from interface import CSP, Constraint, Variable

class IOTools:
  def __init__(self):
    self.file = ""

  def readCSP(self, path: str) -> CSP:
    f = open(path, "r")
    self.file = f.read()
    addend1, addend2, addsum = self.file.split()

    ### variables
    ## carry variables:
    variables = {
      "C" + str(i): Variable(name="C" + str(i), domain=[0, 1]) for i in range(1, len(addsum))
    }
    ## letter variables:
    firstLetters = set([addend1[0], addend2[0], addsum[0]])
    restLetters = set([c for c in self.file if c not in " \n" and c not in firstLetters])
    letterVars = []
    for c in firstLetters:
      variables[c] = Variable(name=c, domain=[i for i in range(1, 10)])
      letterVars.append(variables[c])
    for c in restLetters:
      variables[c] = Variable(name=c, domain=[i for i in range(10)])
      letterVars.append(variables[c])

    ### constraints
    ## allDiff
    allDiff = Constraint(variables=letterVars, evaluate=allDiffConstraint)
    constraints = [allDiff]

    for var in variables.values():
      var.constraints.append(allDiff)
    ## same digit addition
    for i in range(len(addsum)):
      relevantVars = [variables[addsum[-i-1]]]
      kwargs = {
        "result": variables[addsum[-i-1]].name,
        "prevCarry": "",
        "nextCarry": "",
        "addend1": "",
        "addend2": "",
      }
      if i > 0:
        relevantVars.append(variables["C" + str(i)])
        kwargs["prevCarry"] = variables["C" + str(i)].name
      if len(addsum)-1 > i:
        relevantVars.append(variables["C" + str(i+1)])
        kwargs["nextCarry"] = variables["C" + str(i+1)].name
      if len(addend1) > i:
        relevantVars.append(variables[addend1[-i-1]])
        kwargs["addend1"] = variables[addend1[-i-1]].name
      if len(addend2) > i:
        relevantVars.append(variables[addend2[-i-1]])
        kwargs["addend2"] = variables[addend2[-i-1]].name
      digitAdd = Constraint(variables=relevantVars, evaluate=generateAdditionConstraint(**kwargs))
      for var in relevantVars:
        var.constraints.append(digitAdd)
    return (variables, constraints)

  def writeAnswer(self, variable: Variable, path: str):
    f = open(path, "w")
    for c in self.file:
      if c in variable.keys():
        f.write(str(variable[c].value))
      else:
        f.write(c)
    f.close()