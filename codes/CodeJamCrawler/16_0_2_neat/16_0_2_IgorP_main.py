__author__ = 'igor'


class PriorityQueue(object):
    def __init__(self):
        self.list = []

    def append(self, x):
        self.list.append(x)

    def __len__(self):
        return len(self.list)

    def pop(self):
        minVal = float('inf')
        index = -1
        for i in range(0, len(self.list)):
            (state, cost) = self.list[i]
            if cost < minVal:
                minVal = cost
                index = i

        return self.list.pop(index)

class AStar():
    def doSomeMagic(self, initState):
        states = PriorityQueue()
        states.append((initState, 0))
        expanded = []
        while(len(states) > 0):
            (state, cost) = states.pop()
            if state not in expanded:
                expanded.append(state)
                if self.isGoal(state):
                    return cost
                for newState in self.getSuccessors(state):
                    states.append((newState, cost+1))
        return float('inf')

    def getSuccessors(self, state):
        successors = []
        for i in range(0,len(state)):
            successors.append(self.invert(i+1, state))
        return successors

    def invert(self, end,state):
        newState = state[:end][::-1]
        for i in range(len(newState)):
            if newState[i] == '+':
                newState[i] = '-'
            else:
                newState[i] = '+'
        newState = newState+state[end:]
        return newState


    def isGoal(self, state):
        if(state.count("+") == len(state)):
            return True
        return False




def main():
    T = int(input())
    astar = AStar()
    for i in range(T):
        init = list(str(input()))
        state = astar.doSomeMagic(init)
        print("Case #"+str(i+1)+": "+str(state))
main()