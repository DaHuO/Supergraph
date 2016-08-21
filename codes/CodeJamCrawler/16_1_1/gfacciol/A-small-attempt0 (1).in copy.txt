import numpy as np
        

x=open('/Users/facciolo/Downloads/A-small-attempt0.in').read().split()
N = int(x[0])
#print N, x[1:]


for i in range(1,N+1):
    seq = x[i]
    out = seq[0]
    for j in range(1,len(seq)):
        if out[0] > seq[j]:
            out = out + seq[j]
        else:
            out = seq[j] + out

    print "Case #%d: "%i + out