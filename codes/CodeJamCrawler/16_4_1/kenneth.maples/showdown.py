
import sys
sys.setrecursionlimit(5000)
from collections import Counter, defaultdict
from random import choice
import random

DEBUG=True

def gl():
    return sys.stdin.readline().strip()

def expand(q):
    if isinstance(q, list):
        return [expand(q[0]), expand(q[1])]
    if q == 'P':
        return ['P', 'R']
    if q == 'S':
        return ['P', 'S']
    if q == 'R':
        return ['R', 'S']
    assert False, str(q)

def resolve(lst):
    if not isinstance(lst, list):
        return lst

    x = resolve(lst[0])
    y = resolve(lst[1])
    if x < y:
        return x + y
    return y + x

def showdown(N, R, P, S):
    while R + P + S > 1:
        alpha2 = R + P - S
        if alpha2 % 2 != 0:
            return 'IMPOSSIBLE'
        alpha = alpha2 / 2
        if alpha > P or (R - alpha) > S or alpha > R or alpha < 0:
            return 'IMPOSSIBLE'
        R, P, S = R - alpha, alpha, P - alpha
        
    winner = R * 'R' + P * 'P' + S * 'S'
    
    tree = winner
    for _ in range(N):
        tree = expand(tree)
    solution = resolve(tree)
    return solution
    
def main():
    T = int(gl())
    for k in range(T):
        N, R, P, S = map(int, gl().split())
        solution = showdown(N, R, P, S)
        print "Case #" + str(k+1) + ": " + solution

if __name__ == '__main__':
    main()

