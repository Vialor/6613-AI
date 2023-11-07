import heapq
import sys
from agent import Agent
from task_environment import TaskEnvironment
from serialization import Serialization

def main():
    serialization_tool = Serialization()
    serialization_tool.deserialize("test/Input1.txt") # sys.argv[0]
    # task_environment = TaskEnvironment(serialization_tool.deserialize(sys.argv[0]))
    # agent = Agent(task_environment)

    # while agent.frontier:
    #     cost, node = agent.popFrontier()
    #     if task_environment.isGoal(node) == 0:
    #         return node
    #     for child in agent.expand(node):
    #         agent.pushFrontier(child, cost + 1)

    # serialization_tool.serialize()
    

if __name__ == "__main__":
    main()