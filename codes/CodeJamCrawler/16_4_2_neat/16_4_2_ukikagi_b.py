# coding: utf-8
import sys
import heapq
import bisect
import operator
from itertools import *
from functools import reduce

# "IMPOSSIBLE"

def read():
  return int(input())

def reads():
  return [int(s) for s in input().split()]

def prod(xs):
  return reduce(operator.mul, xs, 1)

def solve_small(N, K, P):
  result = 0
  for comb in combinations(range(N), K):
    prob = sum(prod(P[i] if i in xs else 1 - P[i] for i in comb) for xs in combinations(comb, K//2))
    result = max(result, prob)
  return result

T = read()

for case in range(1, T+1):
  (N, K) = reads()
  P = [float(s) for s in input().split()]
  # assert(len(P) == N)
  result = solve_small(N, K, P)
  print("Case #{0}: {1}".format(case, result))
