import os
import math
import copy
import sys
from collections import *

os.chdir('/Users/Dana/Downloads')
f = open('A-large.in','r')
fo = open('A.out','w')
T = int(f.readline())

for ite in range(T):
    d = int(f.readline())
    if d==0:
        res = 'INSOMNIA'
    else:
        whole = {'0','1','2','3','4','5','6','7','8','9'}
        s = set(list(str(d)))
        count = 1
        while s!=whole:
            count = count+1
            d1 = d*count
            s = s|set(list(str(d1)))
        res = d1
    print(ite)
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    fo.write(str(res))
    fo.write('\n')
fo.close()

