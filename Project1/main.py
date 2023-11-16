from agent import Agent
from task_environment import TaskEnvironment
SRC_PATH = "test/Input2.txt"
DEST_PATH = "outputs/Output2.txt"

def main():
    task_environment = TaskEnvironment(SRC_PATH)
    agent = Agent(task_environment)

    solutionFound = False
    while agent.frontier:
        node = agent.popFrontier()[1]
        if task_environment.isGoal(node):
            solutionFound = True
            break
        for child in agent.expand(node):
            agent.pushFrontier(child)
    if solutionFound:
        agent.output(DEST_PATH)
    else:
        print("No Solution!")

if __name__ == "__main__":
    main()