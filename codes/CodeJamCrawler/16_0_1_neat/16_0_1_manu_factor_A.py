#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def run(N):
    if N == 0:
        return 'INSOMNIA'
    used = set()
    n = N
    while True:
        # print n
        used = used.union(str(n))
        if len(used) == 10:
            return n
        n += N

def solve():
    N = int(input.readline())
    return run(N)

for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())

