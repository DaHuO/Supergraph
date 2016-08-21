import sys
import os

def digits(n):
    return [int(c) for c in str(n)]

n = int(sys.stdin.readline().strip())
for i in xrange(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        sys.stdout.write('Case #{0}: {1}\n'.format(i+1, 'INSOMNIA'))
        continue

    n = num
    s = set([0,1,2,3,4,5,6,7,8,9])
    while len(s) > 0:
        for d in digits(n):
            if d in s:
                s.remove(d)
        n += num

    sys.stdout.write('Case #{0}: {1}\n'.format(i+1, n-num))


