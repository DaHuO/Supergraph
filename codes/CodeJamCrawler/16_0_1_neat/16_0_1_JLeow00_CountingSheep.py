def check(seen):
    for i in seen:
        if i == 0:
            return False
    return True

f = open('A-large.in', 'r')
fo = open('CSlarge.out', 'w')
t = int(f.readline())
for i in range(t):
    seen = listofzeros = [0] * 10
    n = int(f.readline())
    j=1
    if n != 0:
        while(not check(seen)):
            k = n*j
            for l in str(k):
                seen[int(l)] = 1
            j+=1
        fo.write("Case #%d: %d\n"%((i+1), n*(j-1)))
    else:
        fo.write("Case #%d: INSOMNIA\n"%((i+1)))
f.close()
fo.close()
