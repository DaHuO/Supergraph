from DomainModel.TestCase import TestCase
import collections
import random
import itertools
from fractions import Fraction
import math
import heapq


class R3A:
    def Solve(self):
        def gVal(x):
            return A - x

        A = 100000
        tests = int(input())
        for test in range(tests):
            n = int(input())
            a = list(map(int, input().split()))
            sol = ''
            tot = sum(a)
            b = list((A - y, x) for x, y in enumerate(a))
            heapq.heapify(b)

            while tot > 0:
                tg1 = (tot - 1) / 2.0
                tg2 = (tot - 2) / 2.0
                q1 = heapq.heappop(b)
                q2 = heapq.heappop(b)
                val = gVal(q1[0])
                l = []
                val -= 1
                if val > 0:
                    heapq.heappush(b, (A - val, q1[1]))
                l.append(q1[1])
                tot -= 1
                if val + 1 >= tg1 and gVal(q2[0]) <= tg1:
                    heapq.heappush(b, q2)
                else:
                    val = gVal(q2[0])
                    val -= 1
                    if val > 0:
                        heapq.heappush(b, (A - val, q2[1]))
                    l.append(q2[1])
                    tot -= 1
                for i in l:
                    sol += chr(ord('A') + i)
                sol += ' '

            print("Case #{}: {}".format(test + 1, sol.strip()))

    def Tests(self):
        yield TestCase("""4
13
1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
""", """Case #1: AB BA
Case #2: AA BC C BA
Case #3: C C AB
Case #4: BA BB CA
    """)
