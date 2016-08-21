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

def lowest_nontrivial_divisor(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return d
        d += 1
    return None

def check(digits):
    mtrace(digits)
    divisors = []
    for base in range(2, 11):
        num = int(digits, base)
        mtrace('  in base', base, 'is', num)
        lnd = lowest_nontrivial_divisor(num)
        if lnd is None:
            mtrace('       which is prime, so digits are not a jamcoin')
            return False
        else:
            mtrace('       which has divisor', lnd)
            divisors.append(lnd)
    assert len(divisors) == 9
    print digits, ' '.join(str(d) for d in divisors)
    return True

n_cases = int(getline())
mtrace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    mtrace()
    atrace( 'Case #', case_num )

    (N,J) = map(int, getline().split())
    mtrace(N,J)

    print 'Case #%d:' % case_num
    n_jamcoins_found = 0
    for i in xrange(pow(2, N-2)):
        fo = '0' + str(N-2) + 'b'
        digits = '1' + format(i, fo) + '1'
        is_a_jamcoin = check(digits)
        if is_a_jamcoin:
            n_jamcoins_found += 1
            atrace(n_jamcoins_found)
            if n_jamcoins_found == J:
                break

    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab ai
