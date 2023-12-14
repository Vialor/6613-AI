def allDiffConstraint(**kwargs: int):
  valList = kwargs.values()
  return any([val == -1 for val in valList]) or len(set(valList)) == len(valList)

def additionConstraint(**kwargs: int):
  return any([val == -1 for val in kwargs.values()]) \
    or kwargs.addend1, kwargs.addend2 + kwargs.prevCarry == kwargs.nextCarry * 10 + kwargs.result[3]
