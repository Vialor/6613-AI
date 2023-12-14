from interface import Variable, Variables


def allDiffConstraint(*vars: Variable):
  valList = [v.value for v in vars]
  return any([v.value == -1 for v in vars]) or len(set(valList)) == len(valList)


def generateAdditionConstraint(addend1: str, addend2: str, prevCarry: str, nextCarry: str, result: str):
  def additionConstraint(*vars: Variable):
    if any([v.value == -1 for v in vars]):
      return True
    valueBook = { v.name: v.value for v in vars }
    fetchValue = lambda name: 0 if name == "" else valueBook[name]
    return fetchValue(addend1) + fetchValue(addend2) + fetchValue(prevCarry) == \
      fetchValue(nextCarry) * 10 + fetchValue(result)
  return additionConstraint