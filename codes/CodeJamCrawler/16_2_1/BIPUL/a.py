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

def solve(a,n):
    return len(a)

for t in range(int(input())):
    #n = int(input())
    #a = [int(i) for i in input().strip().split(" ")]
    s = input()
    num = {chr(c):0 for c in range(65,91)}
    digit = [0 for i in range(10)]
    letter = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    seq = ['Z','W','U','X','F','V','R','G','I','O']
    d = [0,2,4,6,5,7,3,8,9,1]
    for c in s:
        num[c]+=1
    for i in range(10):
        count = num[seq[i]]
        digit[d[i]]=count
        for j in letter[d[i]]:
            num[j]-=count
    print("Case #{0}: ".format(t+1),file=fout,end="")
    for i in range(10):
        for j in range(digit[i]):
            print(i,file=fout,end="")
    print("",file=fout)

######################## PROGRAM END #############################
fin.close()
fout.close()
print("Program complete")
