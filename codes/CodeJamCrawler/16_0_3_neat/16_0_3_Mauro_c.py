from itertools import *
import primefac

def gen_candidates(N):
    start = int('1' + '0'*(N-2) + '1', 2)
    end = int('1' + '0'*N, 2)
    for i in xrange(start, end, 2):
        yield format(i, 'b')

def is_jamcoin(string):
    ret = []
    for b in range(2,11):
        x = int(string, b)
        factor = primefac.primefac(x).next()
        if factor == x: #prime
            return None
        ret.append(str(factor))
    return (string, ret)

def solve(N,J):
    return list(islice((c for c in imap(is_jamcoin, gen_candidates(N)) if c), J))
        
for case in range(int(raw_input())):
    N_length, J_jamcoins = map(int,raw_input().split())
    ans = solve(N_length, J_jamcoins)
    print "Case #%d:" % (case+1,)
    for (string, factors) in ans:
        print string, ' '.join(factors)
        
