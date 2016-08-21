def cal(N):
    if N==0:
        return "INSOMNIA"
    N1=N
    s=set()
    c=2
    while len(s)!=10:
        n=N1
        while n:
            s.add(n%10)
            n=n/10
        N1=N*c
        c=c+1
    return str((c-2)*N)
    

n=int(input())
count=1
while n:
    n=n-1
    N=int(input())
    print "Case #%d: %s" %(count , cal(N))
    count=count+1