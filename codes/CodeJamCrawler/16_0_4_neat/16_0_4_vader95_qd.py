t = int(raw_input())

for i in range(t):
    k, c, s = map(int, raw_input().strip().split())
    if c == 1:
        if s != k:
            res = "IMPOSSIBLE"
        else:
            res = " ".join(str(1+i) for i in range(k))
    else:
        ns = range(2,k**2,2*(k+1))
        if k%2:
            ns.append(k**2)
        if len(ns) > s:
            res = "IMPOSSIBLE"
        else:
            res = " ".join(map(str, ns))
    print "Case #{}: {}".format(i+1,res)
