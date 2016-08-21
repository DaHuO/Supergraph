import itertools
import math
import sys

def is_prime(N):
    for x in xrange(2, int(math.sqrt(N)) + 1):
        if N % x == 0:
            return (False, x)
    return (True, None)

def get_coinjams(N, J):
    coinjams = []
    ss = [''.join(s) for s in itertools.product('01', repeat=(N-2))]
    for s in ss:
        s = '1' + s + '1'
        ps = [is_prime(int(s, b)) for b in range(2, 11)]
        if all([not p[0] for p in ps]):
            coinjams.append((s, [p[1] for p in ps]))
            if len(coinjams) == J:
                break
    return coinjams
 
T = int(sys.stdin.readline())
for t in xrange(T):
    (N, J) = [int(x) for x in sys.stdin.readline().split()]
    print 'Case #' + str(t+1) + ':'
    coinjams = get_coinjams(N, J)
    for (coinjam,divisors) in coinjams:
        print coinjam + ' ' + ' '.join([str(d) for d in divisors])
