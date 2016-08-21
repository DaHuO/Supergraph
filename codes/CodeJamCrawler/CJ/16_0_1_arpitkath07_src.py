def f(n):
    if n==0:
        return "INSOMNIA"
    s=set()
    for i in range(1,300):
        t=list(str(i*n))
        for j in t:
            s.add(j)
        if len(s)==10:
            return i*n
t=int(input())
for i in range(t):
    n=int(input())
    print ("Case #%s: %s"%(str(i+1),str(f(n))))
