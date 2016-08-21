#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

class Bunch:
    def __init__( self, **kwds ):
        self.__dict__ = kwds


pause_after_trace = False
def mtrace(*strs):
    return
    atrace(*strs)

def atrace(*strs):
    f = sys.stderr
    print >> f, '..',
    for str in strs:
        print >> f, str,
    print >> f
    if pause_after_trace:
        response = raw_input('? ')
        if response == 'q':
            sys.exit(1)

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            mtrace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            mtrace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

# ------------------------------------------------------------------------------

if 0:
    # exploratory
    max_N = 10000

    for N in range(max_N):
        max_i = pow(10,2*len(str(N)))
        digits_seen_so_far = set()
        for i in range(1, max_i+1):
            product = N * i
            digits = set(str(product))
            digits_seen_so_far |= digits
            # mtrace(i, product, digits_seen_so_far)
            if len(digits_seen_so_far) == 10:
                answer = product
                break
        else:
            answer = 'INSOMNIA'
        if i > 20:
            mtrace("%2d %2d %4d %s" % (N, i, product, answer))

    # For N<=1000, the highest multiplier I saw was 72, for N=125.
    # And N=0 had the only INSOMNIA.
    sys.exit(1)

n_cases = int(getline())
mtrace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    mtrace()
    atrace( 'Case #', case_num )

    N = int(getline())

    max_i = pow(10,2*len(str(N)))
    mtrace(N, max_i)
    digits_seen_so_far = set()
    for i in xrange(1, max_i+1):
        product = N * i
        digits = set(str(product))
        digits_seen_so_far |= digits
        mtrace(i, product, digits_seen_so_far)
        if len(digits_seen_so_far) == 10:
            answer = product
            break
    else:
        answer = 'INSOMNIA'

    print 'Case #%d: %s' % (case_num, answer)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab ai
