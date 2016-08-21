import sys
import os

def digits(n):
    return [int(c) for c in str(n)]

n = int(sys.stdin.readline().strip())
for i in xrange(n):
    plates = sys.stdin.readline().strip()
    plates = plates[::-1]
    start = '+'

    count = 0
    for plate in plates:
        if plate == start:
            continue
        else:
            count += 1
            if start == '+':
                start = '-'
            else:
                start = '+'

    sys.stdout.write('Case #{0}: {1}\n'.format(i+1, count))
