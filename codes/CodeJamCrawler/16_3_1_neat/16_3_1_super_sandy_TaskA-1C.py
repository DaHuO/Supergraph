from itertools import combinations

def valid(j, val):
    x = {k:v for k,v in val.items()}
    
    #print x, j
    for i in j:
        x[i]-=1
    y = sum(x.values())
    #print x
    if any(v > 0.5*y for v in x.itervalues()):
        return False, val
    else:
        return True, x



t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    al = map(chr, range(65, 65+n))
    s = map(int, raw_input().split())
    d={}
    for j in range(n):
        d[al[j]] = s[j]
    x = list(combinations(al,2)) + al
    k=[]
    while sum(d.values()):
        for j in x:
            b, d = valid(j, d)
            if b:
                k.append(''.join(j))
        #print d
    
    v = ' '.join(k)    
    print "Case #{}: {}".format(i+1,v)

