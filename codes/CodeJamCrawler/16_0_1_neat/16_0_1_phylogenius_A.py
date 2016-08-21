import sys
import itertools as it

for x in range(1, int(sys.stdin.readline()) + 1):
    s = set()
    c = it.count()
    N = int(sys.stdin.readline())
    for i in range(1, 101):
        s = s.union(set(str(i * N)))
        if len(s) == 10:
            break
    print('Case #{}: {}'.format(x, i * N if len(s) == 10 else 'INSOMNIA'))
