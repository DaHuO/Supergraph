from __future__ import print_function
from array import *
from scipy.spatial import ConvexHull
import math
import random
import sys
import argparse

debug = True

def pr(s,end=None):
    if debug==True:
        if end!=None:
            print(s,end=end,flush=True, file=sys.stderr)
        else:
            print(s,flush=True, file=sys.stderr)

def out(s,end=None):
    if end!=None:
        print(s,end=end,flush=True)
    else:
        print(s,flush=True)

def compute(bs,n):
    pass

T = int(input())
for t in range(1, T+1):
    out("Case #" + str(t) + ": ",end="")
    s = input()
    p = ""

    for i in range(len(s)):
        if p=="":
            p+=s[i]
        else:
            if s[i] >= p[0]:
                p = s[i] + p
            else:
                p = p + s[i]
    out(p)
    # b,n = [ int(s) for s in input().split() ]
    # bs =  [ int(s) for s in input().split() ]
    # out(compute(bs,n))
