from collections import deque
from heapq import heappush,heappop
import numpy as np
from math import sqrt

t = int(input())

def bumpComp(orig, pat):
    return pat.replace('1', '.' * len(orig)).replace('0', orig).replace('.', '1')

for i in range(t):

    k,c,s = input().split(' ')
    k = int(k)
    c = int(c)
    s = int(s)


    #print(original)

    tiles = []
    for student in range(s):
        tiles.append(student * (k ** (c-1)) + 1)
    print("Case #{0}: {1}".format(i+1, str(tiles)[1:-1].replace(',',''))) 



    # LGL
    # 1 
    # LGL GGG LGL - GGG GGG GGG - LGL GGG LGL

    # original = [bin(x) for x in range(2**k)]
    # original = [x.replace('0b', '0' * (k-len(x)+2)) for x in original]
    # dfc = []
    # for orig in original:
        
    #     t = orig
    #     for l in range(2,c+1):
    #         t = bumpComp(orig, t)
    #     dfc.append((orig, t))
   
    # print(dfc)



    #print("Case #{0}:".format(i+1))

    