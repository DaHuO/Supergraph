import numpy as np
# from itertools import permutations
# outF = open("D-small-attempt0.out","w")
outF = open("D-small.out","w")

verbose = 0
with open("D-small-attempt0.in","r") as inF:
# with open("D.in","r") as inF:
    t= int(inF.readline())
    for it in xrange(t):
        k, c, s = map(int, inF.readline().split())
        k=long(k)
        if c==1:
            epo=list(np.arange(1,k+1))
        if k==1:
            epo=[1]
        else:
            po=k*(pow(k,(c-1))-1)/(k-1)
            print po
            # print type(po)
            epo=np.arange(1,k+1)
            print epo
            f=po*(epo-1)+epo
            f[0]=1
            print f

            epo=list(f)
            print epo
            
        # print k,c

        outF.write("Case #%d: %s\n"%((it+1), " ".join(str(w) for w in epo)))
        print epo


outF.close()

print "done"