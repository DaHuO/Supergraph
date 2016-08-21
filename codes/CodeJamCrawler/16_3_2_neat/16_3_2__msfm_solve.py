#!/usr/bin/env python3
import sys
import logging


def solve(problem):
    b,m=map(int,problem.split())

    if 2**(b-2) < m:
        return "IMPOSSIBLE"

    answer = ["POSSIBLE"]

    # Connections from the first node
    if m==2**(b-2):
        answer += ["0" + "1"*(b-1)] 
    else:
        answer += [bin(m<<1)[2:].zfill(b)]

    for node in range(2,b+1):
        answer.append("0"*(node) + "1"*(b-node))

    return "\n".join(answer)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    T = int(sys.stdin.readline())
    for t in range(T):
        problem = sys.stdin.readline()
        answer = solve(problem)
        print("Case #{}: {}".format(t+1, answer))
