#! /usr/bin/env python3
import itertools

newline = False


def read_problem():
    n, k = map(int, input().split())
    p = map(float, input().split())
    return (n, k, p)


def prod(l):
    pr = 1
    for p in l:
        pr *= p
    return pr


def tieprob(com, k):
    prob = 0
    for yes in itertools.combinations(range(k), k // 2):
        prob += prod((com[i] if i in yes else (1 - com[i])) for i in range(k))
    return prob


def solve(problem):
    _, k, probs = problem
    maxp = 0
    for com in itertools.combinations(probs, k):
        p = tieprob(com, k)
        if p > maxp:
            maxp = p
    return maxp


def print_solution(solution):
    print(solution)


cases = int(input())
for n in range(1, cases + 1):
    problem = read_problem()
    solution = solve(problem)
    print("Case #{0}:".format(n), end='\n' if newline else ' ')
    print_solution(solution)
