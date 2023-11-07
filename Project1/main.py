import heapq
import sys
from agent import Agent
from task_environment import TaskEnvironment
from serialization import Serialization

def main():
    path = "test/Input1.txt"
    serialization_tool = Serialization()
    task_environment = TaskEnvironment(*serialization_tool.deserialize(path)) # sys.argv[0]
    h = task_environment.calculateHeuristic(task_environment.init_state)
    print(h)
    agent = Agent(task_environment)

    # while agent.frontier:
    #     cost, node = agent.popFrontier()
    #     if task_environment.isGoal(node) == 0:
    #         return node
    #     for child in agent.expand(node):
    #         agent.pushFrontier(child, cost + 1)

    # serialization_tool.serialize()
    

if __name__ == "__main__":
    main()