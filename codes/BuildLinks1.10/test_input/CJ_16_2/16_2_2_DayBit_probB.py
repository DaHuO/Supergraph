'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleB.txt")
f=open("B-small-attempt0.in")
#f=open("B-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    [c,j] = f.readline().split() #[x=='+' for x in f.readline().strip()[::-1]]
    P.append((c,j))

def isValid(c1, c2):
    for i in range(len(c1)):
        if c1[i]!='?' and c2[i]!='?' and c1[i]!=c2[i]:
            return False
    return True
        
def compatible(sn):
    nd = len(sn)
    res = []
    for i in range(0,10**nd):
        if isValid(sn, ('0'*nd+str(i))[-nd:]):
            res.append(('0'*nd+str(i))[-nd:])
    return res
        
    
def solve(s):
    (c,j) = s
    #print(compatible(c))
    #print(compatible(j))
    dif=10e100
    cc1 = cc2 = 0
    nd = len(c)
    for cc_ in compatible(c):
        cc = int(cc_)
        for jj_ in compatible(j):
            jj= int(jj_)
            #print(cc,jj,abs(cc-jj),dif)
            dif2 = abs(cc-jj)
            if dif2<dif:
                cc1 = cc
                jj1 = jj
                dif = dif2
            elif dif2==dif and (cc<cc1 or cc==cc1 and jj<jj1):
                cc1 = cc
                jj1 = jj
                dif=dif2
            
    return ' '.join([('0'*nd+str(cc1))[-nd:],('0'*nd+str(jj1))[-nd:]])
        
fRes = open("res.txt", "w")
case=0
for p in P:
    print("[{0}]".format(p))
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()