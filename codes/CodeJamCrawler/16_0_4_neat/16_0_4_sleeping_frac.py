def to_k(s,k):
    x=1
    for i in range(len(s)):
            x+=int(s[i])*k**(len(s)-i-1)
    return x

t=int(raw_input())

for i in range(t):
    k,c,s=map(int,raw_input().split())
    print "Case #%s:" % (i+1),
    if s<float(k)/c:
        print "IMPOSSIBLE"
        continue
    if s==k:
        print " ".join(map(str,range(1,s+1)))
        continue
    if c>=k:
        print to_k("".join(map(str,range(k))),k)
        continue
    for j in range(k/c):
##        print '{'+"".join(map(str,range(j*c,(j+1)*c)))+'}'
        print to_k("".join(map(str,range(j*c,(j+1)*c))),k),
    if k%c:
##        print '{'+"".join(map(str,range((k/c)*c,k)))+'}'
        print to_k("".join(map(str,range((k/c)*c,k))),k)
    else: print
    
                   
