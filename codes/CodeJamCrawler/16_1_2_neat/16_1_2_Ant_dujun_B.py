import os
import sys

if __name__ == '__main__':
    with open('B-large.in') as w:
        T = w.readline()
        T = int(T.strip())
        for i in xrange(T):
            res = {}
            final_res = []
            N = int(w.readline().strip())
            for j in xrange(2*N-1):
                a = w.readline().strip().split()
                for item in a:
                    if item in res:
                        res[item] += 1
                    else:
                        res[item] = 1
            for k, v in res.iteritems():
                if v % 2:
                    final_res.append(int(k))
            print 'Case #%s: %s' % (i+1, ' '.join([str(item) for item in sorted(final_res)]))
