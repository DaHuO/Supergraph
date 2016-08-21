#!/usr/bin/env python3
import sys
import logging
import string


def solve(problem):
    numbers = map(int,problem.split())
    problem = sorted(list(map(list,zip(numbers,string.ascii_uppercase))), reverse = True)
    
    answer = ""
    while problem[0][0]!=0:
        if (len(problem) == 2) or (problem[2][0] == 0) and (problem[0][0] == problem[1][0]):
            # take 2
            answer += problem[1][1] 
            problem[1][0] -= 1

        answer += problem[0][1] 
        problem[0][0] -= 1

        answer += " "
        problem=sorted(problem, reverse=True)

    return answer.strip()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    T = int(sys.stdin.readline())
    for t in range(T):
        sys.stdin.readline() # throw away
        problem = sys.stdin.readline()
        answer = solve(problem)
        print("Case #{}: {}".format(t+1, answer))
