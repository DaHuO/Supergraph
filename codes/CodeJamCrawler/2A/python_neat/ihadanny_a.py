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
def get_sons(s):
    ret = ''
    for c in s:
        if c == 'P':
            ret += 'PR'
        if c == 'R':
            ret += 'RS'
        if c == 'S':
            ret += 'PS'
    a,b = ret[:len(s)/2+1], ret[len(s)/2+1:]
    #print(ret,a,b)
    return min(a,b) + max(a,b)
    
case = 1
for case in range(1, T+1):
    N,R,P,S = map(int, sys.stdin.readline().strip().split())
    options = []
    for winner in 'PRS':
        players = winner
        for i in range(N):
            players = get_sons(players)
        c = Counter(players)
        #print(c, N, R, P, S, file=sys.stderr)
        if c['R'] == R and c['P'] == P and c['S'] == S:
            dis = 1
            for i in range(N):            
                dis *= 2
                new_players = ""
                #print(dis)
                for j in range(0, len(players), dis):
                    a,b = players[j:j + dis/2], players[j+ dis/2: j + dis]
                    #print(players, j, a,",",b)
                    new_players += min(a,b) + max(a,b)
                players = new_players
            options.append(players)
    if len(options) == 0:
        print("Case #{0}:".format(case), "IMPOSSIBLE")
    else:
        w = min(options)
        print ("Case #{0}:".format(case), w)