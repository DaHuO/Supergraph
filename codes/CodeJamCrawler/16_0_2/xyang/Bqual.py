import os
import math
import copy
import sys
from collections import *

os.chdir('/Users/Dana/Downloads')
f = open('B-small-attempt0.in','r')
fo = open('B.out','w')
T = int(f.readline())

for ite in range(T):
    d = list(f.readline())
    if ite<T-1:
        del d[-1]
    n = len(d)
    for i in range(n):
        if d[i]=='+':
            d[i] = 1
        else:
            d[i] = 0
    res = 0
    while 0 in d:
        for i in range(n):
            if d[i]==0:
                pos = i
        if d[0]==1:
            i = 1
            while d[i]==1:
                i = i+1
            d[:i] = [0]*i
        else:
            temp = d[:pos+1]
            temp = temp[::-1]
            for i in range(len(temp)):
                if temp[i]==0:
                    temp[i] = 1
                else:
                    temp[i] = 0
            d = temp+d[pos+1:]
        res = res+1 
    print(ite)
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    fo.write(str(res))
    fo.write('\n')
fo.close()

