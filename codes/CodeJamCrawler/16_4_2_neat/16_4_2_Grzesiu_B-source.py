import imp, sys

sys.modules["utils"] = __mod = imp.new_module("utils")
exec """#!/usr/bin/python

from itertools import chain, repeat, izip

def line(*args):
	L = raw_input().strip().split()
	L = izip( L, chain( args, repeat(str) ) )
	return [ type(data) for data, type in L ]	
	
def iline(): return map( int, raw_input().strip().split() )
def fline(): return map( float, raw_input().strip().split() )""" in vars(__mod)

#!/usr/bin/python

from utils import iline, fline
from sys import stderr

def test():
    N, K = iline()
    P_ = fline()
    
    yield
    
    P_.sort()
    answer = 0.0
    for n in xrange(K+1):
        P = P_[:n] + (P_[-K+n:] if n != K else [])
        #print >>stderr, P
        F = { 0: 1.0 }
        for p in P:
            score = lambda p, x : p*F.get(x-1, 0.0) + (1-p)*F.get(x, 0.0)
            F = { x: score(p, x) for x in xrange(N) }
            
        answer = max(answer, F[K/2])
        
    print '{:.12f}'.format(answer)        
        
if __name__ == '__main__':
    T = input()
    for i in xrange(1, T+1):
        print 'Case #%d:' % i,
        solver = test()
        if hasattr(solver, 'next'):
            list(solver)
        elif callable(solver):
            solver()

