import numpy as np
        

x=open('pan2.txt').read().split()
N = int(x[0])
print N, x[1:]


for i in range(1,N+1):
    seq = x[i]
    c = 0
    p = 0
    if seq[0] == '-':
        p = 1;
    
    for j in range(len(seq)-1):
        if(seq[j] != seq[j+1]):
            c = c+1
            p = p+1

    c = c + p%2
    
    
    print "Case #%d: %d"%(i,c)
