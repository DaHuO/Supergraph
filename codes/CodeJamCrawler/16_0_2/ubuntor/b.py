import sys
import itertools
l = [i for i in open(sys.argv[1]).read().strip().split()[1:]]
out = ''
for i,n in enumerate(l):
    n = n.rstrip('+')
    ans = len([i for i in itertools.groupby(n)])
    out += 'Case #{}: {}\n'.format(i+1,ans)
open('B.out','w').write(out)
