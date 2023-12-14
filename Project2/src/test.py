from iotools import IOTools
io = IOTools()
variables, constraints = io.readCSP("../test/input1.txt")
io.writeAnswer(variables, "../test/output1.txt")