from interface import Variables


def printVars(vars: Variables):
  for name, var in vars.items():
    print(name, var.value, end="; ")
  print("\n")