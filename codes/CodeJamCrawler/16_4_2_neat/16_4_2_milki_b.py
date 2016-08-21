from collections import defaultdict
from itertools import combinations as comb

def main():
    T = int(raw_input())
    for i in xrange(T):
        N, K = map(int, raw_input().split())
        P = map(float, raw_input().split())
        # print N, K, P        
        max_p = 0
        for kk in comb(range(N), K):
            # print 'pick K', kk
            this_p = 0
            for yes in comb(kk, len(kk) / 2):
                # print '  pick yes', yes
                p = 1.0
                for idx in kk:
                    if idx in yes:
                        p *= P[idx]
                    else:
                        p *= (1-P[idx])
                this_p += p
                # print '  p', p
            # print '  this_p', this_p
            max_p = max(max_p, this_p)
        output(i, max_p)


def output(casenum, ret):
    print 'Case #%d: %f' % (casenum + 1, ret)


main()
