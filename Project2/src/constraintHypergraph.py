class Variable:
  def __init__(self, name: str):
    self.name = name
    self.constraints = []

class Constraint:
  def __init__(self):
    self.variables = []
    self.evaluate
    