#!/usr/bin/python

import sys



def find_factor(n, k):
    for f in xrange(2, min(k+2, n)):
        if n % f == 0:
            return f
    return False

if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = f.readlines()
        N, J = [int(v) for v in lines[1].split(' ')]

    bases = {b: [b ** x for x in xrange(N)] for b in xrange(2, 11)}
    #print bases

    def tobase(b, n):
        ''' return n in base b) '''
        #print [bases[b][i] * int(d) for i, d in enumerate(n[::-1])]
        return sum([bases[b][i] * int(d) for i, d in enumerate(n[::-1])])

    i0 = eval('0b1' + '0' * (N - 1)) + 1
    out = {}
    thr = 1000
    i = 0

    while len(out) < J:
        # find J coins
        #loop through all candidate coins
        #try to find factors
        factors = []
        n = bin(i0 + i)[2:]
        for b in bases:
            #print 'checking', bin(i0 + i), 'in base', b
            #print 'n:', n, 'base', b, ':', tobase(b, n)
            f = find_factor(tobase(b, n), thr)
            if f:
                factors.append(f)
        if len(factors) == 9:
            #print 'found', n, factors
            out[n] = factors
        i += 2

    outlines = ['Case #1:']
    for n, f in out.items():
        outlines.append('%s %s' % (n, ' '.join([str(v) for v in f])))

    with open(fname[:-2] + 'out', 'w') as f:
        f.write('\n'.join(outlines))

