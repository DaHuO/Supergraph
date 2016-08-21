T=int(raw_input())

for i in range(T):
    p=i+1
    L=[]
    M=[]
    n=(raw_input())
    o=0
    for j in range(1,11111):

        m=str(j*int(n))

        x=list(m)
        L=L+x
        S=set(L)
        M=sorted(list(S))
        if(M==['0','1','2','3','4','5','6','7','8','9']):
            o= m
            break
        elif(M==['0']):
            o="INSOMNIA"
            break

    print "Case #%s: %s" %(p,o)

