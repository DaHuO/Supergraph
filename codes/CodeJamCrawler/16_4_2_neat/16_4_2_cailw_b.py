from __future__ import print_function, division
from itertools import combinations

title='b'

with open('%s.txt'%title) as fi, open('%s_o.txt'%title,'w') as fo:
    def readint():
        return int(fi.readline().strip())
    def readints():
        return list(map(int,fi.readline().split()))
    def readfloats():
        return list(map(float,fi.readline().split()))
    t=readint()
    for icase in range(1,t+1):
        def print_case(*args):
            print('Case #%d:'%icase,*args,file=fo)
        n,k=readints()
        p=readfloats()
        ans=0
        for ix in combinations(list(range(n)),k):
            genfun=[1]
            for i in ix:
                genfun=[(1-p[i])*genfun[0]]+[p[i]*genfun[j-1]+(1-p[i])*genfun[j] for j in range(1,len(genfun))]+[p[i]*genfun[-1]]
            ans=max(ans,genfun[k//2])
        print_case(ans)
