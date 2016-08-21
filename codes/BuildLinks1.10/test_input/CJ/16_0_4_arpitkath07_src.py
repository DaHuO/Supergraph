def f(n):
    return " ".join(str(i) for i in range(1,n+1))
t=int(raw_input())
for i in range(t):
    a,b,c=map(int,raw_input().split())
    print ("Case #%d: %s"%(i+1,f(a)))