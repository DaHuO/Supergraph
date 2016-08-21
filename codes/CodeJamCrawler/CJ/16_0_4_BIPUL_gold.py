############### Author: Bipul Ranjan @ranjanbipul ###############
import sys
import time
import os
import math
import operator
import random
from functools import lru_cache
from decimal import Decimal as D
from fractions import Fraction as F
#sys.setrecursionlimit(10000)
#@lru_cache(maxsize=None)
MOD = 1000000007
################################################################
QNO = 'd' #SET QUESTION NUMBER
FIN,FOUT = QNO+'.in.txt',QNO+'.out.txt'
FIN = QNO.capitalize()+'-small-attempt0.in'
#FIN = QNO.capitalize()+'-large.in'
fin = open(FIN)
fout = open(FOUT,'w')
sys.stdin = fin
######################## PROGRAM  START ##########################

for t in range(int(input())):
    (K,C,S) = [int(s) for s in input().strip().split(' ')]
    last = pow(K,C-1)
    out = [str(i*last) for i in range(1,S+1)]
    print("Case #{0}: {1}".format(t+1," ".join(out)),file=fout)
######################## PROGRAM END #############################
fin.close()
fout.close()
print("Program complete")
