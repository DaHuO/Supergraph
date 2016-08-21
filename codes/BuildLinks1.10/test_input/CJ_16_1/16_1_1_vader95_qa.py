def lastword(s):
    ns = s[0]
    for c in s[1:]:
        ns = max(c+ns, ns+c)
    return ns
    
t = int(raw_input())

for i in range(t):
    print "Case #{}: {}".format(i+1, lastword(raw_input().strip()))
