import sys


class BFSSolver:

    @staticmethod
    def solve(initialState):
        solution = BFSSolver.bfs(initialState)
        if solution is None:
            return None
        arr = [solution]
        while solution.parent is not None:
            solution = solution.parent
            arr.append(solution)
        reversedArr = arr[::-1]
        return reversedArr

    @staticmethod
    def bfs(initialState):
        frontier = [initialState]
        initialState.parent = None
        initialState.level = 0
        visited = {initialState}
        totalVisited = 0
        while frontier:
            totalVisited = totalVisited + 1
            selected = frontier[0]

            del frontier[0]
            if selected.is_goal():

                return selected

            branches = selected.get_next_states()

            for b in branches:

                if b not in visited:
                    visited.add(b)
                    b.parent = selected
                    b.level = selected.level + 1
                    frontier.append(b)



import copy

class SideState:

    def __init__(self,int_str, level=0):
        if type(int_str)== str:
            self.int_str=[]
            for i in int_str:
                if i == "+":
                    self.int_str.append(True)
                else:
                    self.int_str.append(False)
        else:
            self.int_str = int_str
        self.level= level


    def get_next_states(self):
        for i in range(1,len(self.int_str)+1):
            first = self.int_str[:i][::-1]
            second = self.int_str[i:]
            first = [not i for i in first]
            last =first+second
            a_state=SideState(last, self.level+1)
            yield copy.deepcopy(a_state)


    def is_goal(self):
        if all(self.int_str):
            return True
        else:
            return False

    def getCost(self):
        return self.int_str.count(True)


    def __lt__(self, other):
        return self.getCost() < other.getCost()

    def __eq__(self, other):
        return (self.int_str==other.int_str)

    def __str__(self):
        return str(self.int_str)

    def __hash__(self):
        return hash(str(self.int_str))




# check out .format's specification for more formatting options
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for i in xrange(1,t+1):
    n = raw_input().split(" ")[0]  # read a list of integers, 2 in this case
    # for each first, second, third digits of number..
    p = SideState(n)

    result= BFSSolver.solve(p)



    print "Case #{}: {}".format(i, result[-1].level)
