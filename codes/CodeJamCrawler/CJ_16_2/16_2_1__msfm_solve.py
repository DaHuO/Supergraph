#!/usr/bin/env python3
import sys
import logging


def solve(problem):
    answer = []
    problem=list(problem)
    first ={ 'Z':('0','ZERO'), 'W':('2','TWO'), 'U':('4','FOUR'), 'X':('6','SIX'), 'G':('8','EIGHT')}
    second = { 'H':('3','THREE'), 'F':('5','FIVE') }
    third = { 'O':('1', 'ONE'), 'S':('7', 'SEVEN') }
    fourth = { 'I':('9', 'NINE') }

    def unique(s):
        for u in s:
            n=problem.count(u)
            if n>0:
                answer.append(n * s[u][0])
                for l in s[u][1]:
                    for _ in range(n):
                        problem.remove(l)

    unique(first)
    unique(second)
    unique(third)
    unique(fourth)
    #answer.append([problem])
    return "".join(sorted(answer))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    T = int(sys.stdin.readline())
    for t in range(T):
        problem = sys.stdin.readline().strip()
        answer = solve(problem)
        print("Case #{}: {}".format(t+1, answer))
