#!/usr/bin/env python

class Solution(object):
    case = 1
    msg = "Case #{0}: {1}"

    @classmethod
    def show(cls, sol):
        print(cls.msg.format(cls.case, sol))
        cls.case += 1

with open("A-large.in", 'r') as f:
    problems = int(f.readline())

    for p in range(problems):
        n = int(f.readline())
        m = 0

        seen = set()
        times = 0

        for iteration in range(100):
            m += n
            seen.update([int(i) for i in str(m)])
            if len(seen) == 10:
                break

        if len(seen) == 10:
            Solution.show(m)
        else:
            Solution.show("INSOMNIA")


