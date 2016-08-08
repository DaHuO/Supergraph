from __future__ import print_function, division

title='a'

with open('%s.txt'%title) as fi, open('%s_o.txt'%title,'w') as fo:
    def readint():
        return int(fi.readline().strip())
    def readints():
        return list(map(int,fi.readline().split()))
    t=readint()
    for icase in range(1,t+1):
        def print_case(*args):
            print('Case #%d:'%icase,*args,file=fo)
        n,r,p,s=readints()
        if abs(p-r)>1 or abs(r-s)>1 or abs(s-p)>1:
            print_case('IMPOSSIBLE')
            continue
        ss=[['']*3 for _ in range(n+1)]
        ss[1]=['RS','PS','PR']
        def msum(a,b):
            return min(a+b,b+a)
        for i in range(2,n+1):
            ss[i][0]=msum(ss[i-1][1],ss[i-1][2])
            ss[i][1]=msum(ss[i-1][2],ss[i-1][0])
            ss[i][2]=msum(ss[i-1][0],ss[i-1][1])
        if r==s:
            print_case(ss[n][0])
        if s==p:
            print_case(ss[n][1])
        if p==r:
            print_case(ss[n][2])
