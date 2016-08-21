import numpy as np
        

x=open('bela2.txt').read().split()
N = int(x[0])
#print N, x[1:]


        
def test(nbr, r):
    rr = r * nbr 
#    print rr
    
    RRR = map(str,list(rr))
    a = np.zeros(10)
    for t in range(len(r)):
        for c in RRR[t]:
    #        print c
            a[int(c)] = 1
        if np.sum(a) == 10: 
    #        print a
            return rr[t] 
    if np.sum(a) < 10:  
        print 'FAIL %d'%nbr
        print a
    return -1
        

for i in range(1,N+1):
    nbr = int(x[i])
   # nbr = np.random.randint(1,100000000)
    if nbr == 0:
        print "Case #%d: INSOMNIA"%i
        continue
    if nbr == 2:
        r = np.arange(1,51)
        res = test(nbr,r)
        print "Case #%d: %d"%(i,res)
    else:
        r = np.arange(1,150)
        res = test(nbr,r)
        print "Case #%d: %d"%(i,res)
