def solve(K, C, S):
    step = K**(C - 1)
    mid = (step + 1) // 2
    ans = [step * i + mid for i in range(0, S)]
    return ' '.join(map(str, ans))

import sys
sys.stdin = open('D-small-attempt0.in', 'rt')
sys.stdout = open('D-small.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    K, C, S = map(int, raw_input().strip().split(' '))
    print "Case #{}:".format(t), solve(K, C, S)
