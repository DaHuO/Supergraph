# coding: utf-8
import sys
import heapq
import bisect
import operator
from itertools import *

def read():
  return int(input())

def reads():
  return [int(s) for s in input().split()]

T = read()

dic = {'P':"PR", 'R':"RS", 'S':"PS"}

for case in range(1, T+1):
  (N, R, P, S) = reads()
  # "P" < "R" < "S"
  words = ["P", "R", "S"]
  for _ in range(N):
    words = [words[0] + words[1], words[0] + words[2], words[1] + words[2]]

  for word in words:
    if (R == sum(c == 'R' for c in word) and
        P == sum(c == 'P' for c in word) and
        S == sum(c == 'S' for c in word)):
      print("Case #{0}: {1}".format(case, word))
      break
  else:
    print("Case #{0}: {1}".format(case, "IMPOSSIBLE"))
