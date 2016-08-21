L=map(str, raw_input().split())
N=int(L[0])

for x in xrange(N):
    result=0
    y=L[x+1][0]
    flag=True
    for z in L[x+1]:
        if y!=z:
            result+=1
            y=z
    if L[x+1][-1]=='-':
        result+=1
    print "Case #"+str(x+1)+': '+str(result)    
    