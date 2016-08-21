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
QNO = 'a' #SET QUESTION NUMBER
FIN,FOUT = QNO+'.in.txt',QNO+'.out.txt'
FIN = QNO.capitalize()+'-small-attempt0.in'
FIN = QNO.capitalize()+'-large.in'
fin = open(FIN)
fout = open(FOUT,'w')
sys.stdin = fin
######################## PROGRAM  START ##########################
limit = 100

for t in range(int(input())):
    s = int(input())
    if s==0:
        print("Case #{0}: {1}".format(t+1,"INSOMNIA"),file=fout)
    else:
        d=s
        count,loop = 0,0
        num = [False for i in range(10)]
        while True:
            word = str(d)
            for w in word:
                if not num[int(w)]:
                    count+=1
                    num[int(w)]=True
            loop+=1
            if count==10 or loop>limit:
                break;
            d+=s
        if loop>limit:
            print("Case #{0}: {1}".format(t+1,"INSOMNIA"),file=fout)
        else:
            print("Case #{0}: {1}".format(t+1,d),file=fout)

######################## PROGRAM END #############################
fin.close()
fout.close()
print("Program complete")
