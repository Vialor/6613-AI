import heapq
from typing import List
from interface import DIRECTION, Cube


class Agent:
    def __init__(self, task_environment):
        self.node_history = {}  # Cube: minmum total cost (g not f), parent Cube, last move direction
        self.task_environment = task_environment
        self.node_count = 0
        self.frontier = [(0, task_environment.init_state)]  # priority queue: (f=g+h, Cube)
        self.gValue = 0

    def act(self, curState: Cube, direction) -> Cube:
        # if state has been visited # Maybe check against node_history? also check if move is valid
        ## return None
        # else
        ## calculate child by exchanging elems in curState
        # return child
        parent_cube = curState
        tmp_list = []
        i = 0
        while i < 3:
            tmp_list.append(curState[0][i] + direction[i])
            i = i + 1
        i = 0
        while i < 3:

            if tmp_list[i] < 0 or tmp_list[i] > 2:
                pass
            i = i + 1
        tmp_tuple = tuple(tmp_list)
        try:
            index = curState.index(tmp_tuple)
            tmp_tuple2 = curState[index]
            curState[index] = curState[0]
            curState[0] = tmp_tuple2
        except ValueError:
            print(f"{tmp_tuple} is not in the list.")

        if tuple(curState) in self.node_history.keys():
            pass
        self.gValue = self.gValue + 1
        self.node_history[tuple(curState)] = [self.gValue, parent_cube, direction]
        print(curState)
        print("\n")
        return curState

    def expand(self, node):
        children = []
        for direction in DIRECTION.values():
            child = self.act(node, direction)
            if child is not None:
                children.append(child)
        return children

    def popFrontier(self):
        return heapq.heappop(self.frontier)

    def pushFrontier(self, newNode: Cube, parentCost: int):
        fValue = self.task_environment.calculateHeuristic(newNode) + parentCost
        heapq.heappush(self.frontier, (fValue, newNode))
