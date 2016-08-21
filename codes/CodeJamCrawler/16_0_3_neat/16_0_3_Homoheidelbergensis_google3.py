import itertools
import time
from functools import lru_cache

f=open('Test.in', 'r')
out=open('out.out','w')
T=int(f.readline())
N,J=map(lambda x: int(x),f.readline().strip().split(' '))
out.write("Case #1: \n")
poss=list(map(lambda x:list(x),(itertools.product(range(2), repeat=N-2))))

from math import sqrt

count=0
@lru_cache(maxsize=None)
def prim(n):
    i=2
    stop_n = int(sqrt(n))
    while(n%i!=0):
        i+=1
        if i > stop_n:
            return 0
    return i
j=0
bases=[x for x in range(2,11)]
while(count<J):
    t0 = time.clock()
    print(poss[j])
    test=list(map(lambda x:int("1"+"".join(map(lambda x: str(x), poss[j]))+"1",x), bases))
    s=list(map(lambda x: prim(x),test))
    print(time.clock() - t0)
    if 0 not in s:
        out.write("1"+"".join(map(lambda x: str(x), poss[j]))+"1"+"  "+"".join(map(lambda x: str(x)+" ", s)))
        out.write("\n")
        count+=1
    j+=1
