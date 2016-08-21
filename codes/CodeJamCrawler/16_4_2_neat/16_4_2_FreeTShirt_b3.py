def ptie(p, i, j): #index i, jx1
    if j==0:
        s=1
        for z in range(i+1):
            s*=(1-p[z])
        return s
    if i==0 and j==0:
        return 1-p[0]
    if i==0 and j==1:
        return p[0]
    if i==0 and j>1:
        return 0
    return ptie(p, i-1, j)*(1-p[i]) + ptie(p, i-1, j-1)*p[i]

import itertools

fp = open("b2s.txt")
fw = open("b2a.txt", 'w')
t = int(fp.readline().strip())
 
for case in range(t):
    print(case)
    n, k = fp.readline().strip().split()
    n = int(n)
    k = int(k)
    p = fp.readline().strip().split()
    p = sorted([float(x) for x in p])
    p *=2
    pmax=0
    for i in range(n):
        s = p[i:i+k]
        print(n, len(s), k)
        pb = ptie(s, k-1, int(k/2))
        if pb > pmax:
            pmax=pb


#    for s in list(itertools.combinations(p, k)):
#        pb = ptie(s, k-1, int(k/2))
#        if pb > pmax:
#            pmax = pb
    print(pmax)
        
    fw.write("Case #{0}: {1:.10f}\n".format(case+1, pmax))
    
    
#    fw.write("Case #{0}: {1}\n".format(case+1, g))

    
