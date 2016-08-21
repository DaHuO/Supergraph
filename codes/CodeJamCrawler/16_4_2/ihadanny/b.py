from __future__ import print_function
import sys
from collections import defaultdict
from fractions import gcd
from math import factorial
from scipy.optimize import linprog
import numpy as np
import itertools as it
#from graph_tool.all import *
import math
import os.path
import cPickle
from collections import Counter

T = int(sys.stdin.readline())

def tie_prob(chosen, K):
    if len(chosen) < K:
        return 0.0
    if len(chosen) == 0:
        return 1.0
    prob = (1-chosen[0])*tie_prob(chosen[1:], K)
    if K > 0:
        prob += chosen[0]*tie_prob(chosen[1:], K-1)
    return prob
case = 1
for case in range(1, T+1):
    N,K = map(int, sys.stdin.readline().strip().split())
    probs = map(float, sys.stdin.readline().strip().split())
    probs.sort()
    maxi, best = 0.0, []
    for combination in it.product("01", repeat=N):
        chosen = []
        for j in range(N):
            if combination[j] == "1":
                chosen.append(probs[j])
        if len(chosen) != K:
            continue
        cur = tie_prob(chosen, K/2)
        if cur > maxi:
            maxi = cur    
            best = chosen
    chosen = []
    i, j = 0, len(probs)-1
    while len(chosen) < K:
        if probs[i] < 0.5 and probs[j] > 0.5:
            chosen.append(probs[i])
            chosen.append(probs[j])
            i+=1
            j-=1
        else:
            break
    if probs[j] <= 0.5:
        while len(chosen) < K:
            chosen.append(probs[j])
            j-=1
    else:
        while len(chosen) < K:
            chosen.append(probs[i])
            i+=1
    #print ("Case #{0}:".format(case), sorted(probs), K, sorted(chosen), tie_prob(chosen, K/2), sorted(best), maxi)
    print ("Case #{0}:".format(case), maxi)