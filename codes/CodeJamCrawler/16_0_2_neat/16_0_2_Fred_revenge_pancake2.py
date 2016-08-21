from base import *
from heapq import *

"""
Ohh my got this is so horrible,

How can i not see directly the solution.
Screw the hscore as an heuristic, this is the answer, not need for all the
rest
"""

class RevengePancakeSolver (CodeJamSolver):
    def read_instance(self, f):
        return tuple(f.readline().strip())

    def solve_instance(self, input):
        def flip(stack, i):
            def flipone(p):
                return '+' if p == '-' else '-'
            return tuple(list(reversed(map(flipone, stack[:i+1]))) + list(stack[i+1:]))

        def smart_flip(stack):
            for i in range(0, len(stack) -1):
                if stack[i+1] != stack[i]:
                    yield i
            yield len(stack) -1

        def hscore(stack):
            s = 0
            for i in range(0, len(stack) -1):
                if stack[i+1] != stack[i]:
                    s+=1
            return s

        visited = set([input])
        top = [(0, 0, input)]
        m = 10000000
        best = 1000000
        while top:
            h, cost, x = heappop(top)
            # print "pop ", cost, h, x

            if cost > best:
                continue

            if cost + h >= best:
                continue

            if all(map(lambda p:p=='+', x)):
                # print 'Found path len', cost, x
                # return cost
                if best > cost:
                    best = cost
            elif cost > best:
                continue

            if cost + h >= best:
                continue

            for i in smart_flip(x):
                next = flip(x, i)
                if next not in visited:
                    heappush(top, (hscore(next), cost+1, next))
                    visited.add(next)
        return best

if __name__ == '__main__':
    solver = RevengePancakeSolver()
    solver.run()
    # print solver.solve_instance(tuple('---+-+---++-+---++-+---+++---+-+'))


        # i = 0
        # while i < len(stack) -1:
        #     while i < len(stack) -1 and stack[i] == stack[i+1]:
        #         i+=1
        #     print i
        #     i+=1


    # print list(smart_flip(tuple('---+----+-+')))
