def A(N):
    val=N
    dic={k:1 for k in range(10)}
    while not dic=={}:
        s=str(val)
        for i in range(len(s)):
            if int(s[i]) in dic:
                del dic[int(s[i])]
        val=val+N
    return (val-N)
    
T=int(input())
for i in range(T):
    N=int(input())
    if N==0:
        print ('Case #%d: INSOMNIA'%(i+1))
    else:
        print ('Case #%d: %d'%(i+1,A(N)))
    
