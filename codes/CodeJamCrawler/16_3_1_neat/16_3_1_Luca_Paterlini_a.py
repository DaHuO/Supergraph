# -- separate project  --BASE FILE for comp-----------
def readarray(): return map(int,raw_input().split())
from string import ascii_uppercase as tp

def solve():
    n=input()
    v=readarray()
    r=[]
    while sum(v)>3:
        q=v.index(max(v));v[q]-=1
        u=v.index(max(v));v[u] -= 1
        r.append(tp[q]+tp[u])

    if sum(v)==2:
        q = v.index(max(v));v[q] -= 1
        u = v.index(max(v));v[u] -= 1
        r.append(tp[q] + tp[u])
    elif sum(v)==3:
        q = v.index(max(v));v[q] -= 1
        r.append(tp[q])
        q = v.index(max(v));v[q] -= 1
        u = v.index(max(v));v[u] -= 1
        r.append(tp[q] + tp[u])
    else: pass

    return ' '.join(r)









T=input()
for i in range(1,T+1):
    print "Case #%d: %s" %(i,solve())

