import sys
import itertools as it
import math
import random
from collections import Counter

def solve(n):
 ANS = []
 for words in xrange(0,len(n[0])):

    if words == 0:
        ANS.append(n[0][words])
    elif ord(n[0][words]) > ord(ANS[0][0]):
        ANS.insert(0,n[0][words])
    elif ord(n[0][words]) < ord(ANS[0][0]):
        ANS.append(n[0][words])
    elif ord(n[0][words]) == ord(ANS[0][0]):
        ANS.insert(0,n[0][words])
 return ''.join(ANS)




t = int(raw_input())
for i in xrange(1, t + 1):
  n = [str(s) for s in raw_input().split(" ")]
  print "Case #{}: {}".format(i, solve(n))
