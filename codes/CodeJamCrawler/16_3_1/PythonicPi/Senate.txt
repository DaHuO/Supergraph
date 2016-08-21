

L=map(int, raw_input().split())
ctr=0

T=L[ctr]
ctr+=1

Alp=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for x in xrange(1, T+1):
    N=L[ctr]
    P=[]
    ctr+=1
    
    for y in xrange(N):
        P.append(L[ctr])
        ctr+=1
    
    maxP=-1
    
    print "Case #"+str(x)+':',
    
    while max(P)!=0:
        maxP=max(P)
        i=P.index(maxP)
        try:
            if sum(P)%2==0:
                
                j=i+1+(P[i+1:].index(maxP))
                print Alp[i]+Alp[j],
                P[i]-=1
                P[j]-=1
            else:
                print Alp[i],
                P[i]-=1
                
        except:
            j='NaN'
            print Alp[i],
            P[i]-=1
            
        
    print '\t'
    