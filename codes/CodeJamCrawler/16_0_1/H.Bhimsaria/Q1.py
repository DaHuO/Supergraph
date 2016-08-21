def spt(N,a):
    while N:
        x=N%10;
        if x not in a:
            a.append(x)
        N=N//10
               
T=int(raw_input())
z=1
for i in range(0,T):
    a=[]
    N=int(raw_input())
    M=N
    y=1
    if N==0:
        print "Case #%d: INSOMNIA"%z
        z=z+1
        continue
    while len(a)!=10:
        spt(M,a)
        y=y+1
        M=N*y
    M=M-N
    print "Case #%d: %d" %(z,M)
    z=z+1
