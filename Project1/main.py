import heapq
import sys
from agent import Agent
from task_environment import TaskEnvironment

def main():
    path = "test/Input1.txt"
    task_environment = TaskEnvironment(path) # sys.argv[0]
    agent = Agent(task_environment)

    # while agent.frontier:
    #     cost, node = agent.popFrontier()
    #     if task_environment.isGoal(node) == 0:
    #         return node
    #     for child in agent.expand(node):
    #         agent.pushFrontier(child, cost + 1) 
    agent.output("outputs/Output1.txt")

if __name__ == "__main__":
    main()