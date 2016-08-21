import sys
l = [int(i) for i in open(sys.argv[1]).read().strip().split()[1:]]
out = ''
for i,n in enumerate(l):
    s = set()
    ans = 'INSOMNIA'
    for j in range(1,10000): # lol
        s = s.union(set(str(j*n)))
        if len(s) == 10:
            ans = str(j*n)
            break
    out += 'Case #{}: {}\n'.format(i+1,ans)
open('A.out','w').write(out)
