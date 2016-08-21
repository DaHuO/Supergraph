t=int(input())
ns=map(int,[input() for i in range(t)])

ALL = set('1234567890')

for i,n in enumerate(ns):
    if n == 0:
        print("Case #%d: INSOMNIA"%(i+1))
        continue
    t = n
    SEEN = set(str(t))
    while ALL != SEEN:
        t+=n
        SEEN = SEEN.union(str(t))
    print("Case #%d: %d"%(i+1,t))