from collections import defaultdict
def readarray(): return map(int,raw_input().split())

e=("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
def test(dict,val):
    tmp=dict.copy()
    for c in val:
        if dict[c]>0:dict[c]-=1
        else: return [tmp,0]
    return [dict,1]

def fun():
    d=defaultdict(int)
    s=raw_input()
    r=[]
    for c in s:d[c]+=1
    for el in [6,0,2,8,3,7,5,4,1,9]:
        d,a=test(d,e[el])
        while a:
            r.append(str(el))
            d,a=test(d, e[el])
    return ''.join(map(str,sorted(r)))




T=input()
for i in range(1,T+1):
    print "Case #%d: %s" %(i,fun())
