#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')


def solve(S):
    top, S = S[0], S[1:]
    if not S:
        if top == '+':
            return 0
        else:
            return 1
    if top == S[0]:
        return solve(S)
    else:
        return 1+solve(S)
        
def run():
    S = list(input.readline().strip())
    return solve(S)

T = int(input.readline())
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,run())

