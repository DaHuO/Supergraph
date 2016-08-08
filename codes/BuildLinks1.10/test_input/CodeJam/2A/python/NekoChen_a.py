import sys, numpy as np
from itertools import combinations, permutations
from operator import itemgetter
from collections import deque, defaultdict
import heapq

RULE = { ("R", "P"): "P", ("P", "R"): "P", 
         ("P", "S"): "S", ("S", "P"): "S", 
         ("S", "R"): "R", ("R", "S"): "R" }

def tour(b):
    c = []
    for i, j in zip( *([iter(b)]*2) ):
        if i == j: return 
        c.append( RULE[(i,j)] )
    return c

cache = set()

def test(b, s):
    t = "".join(b)
    if t in cache:
        return
    while len(b) > 1:
        b = tour(b)
        if b == None:
            return 
    return s.append(t)

def solve2( N, R, P, S ):
    M = 1<<N
    a = sorted([ (R, "R"), (P, "P"), (S, "S") ], reverse=True)
    b = [ 0 ]*M
    
    n, p  = a[0]
    if n > (M>>1):
        return "IMPOSSIBLE"
    b[:n*2:2] = [p]*n
    
    n1, p1 = a[1]
    b[n*2::2] = [ p1 ]* ( (M>>1) - n )
    
    n1 -= ( (M>>1) - n )
    n2, p2 = a[2]
    
    z = permutations( [p1]*n1 + [p2]*n2 )
    for i in z:
        b[1::2] = i
        if test(b):
            return "".join(b)
    return "IMPOSSIBLE"

def solve( N, R, P, S ):
    z = permutations( ["R"]*R + ["P"]*P + ["S"]*S )
    cache.clear()
    s = []
    for i in z:
        #b[1::2] = i
        #if test(i):
        #    return "".join(i)
        test(i, s)
    if len(s) == 0:
        return "IMPOSSIBLE"
    return min(s)

def main():
    f = open( sys.argv[1] ) if len(sys.argv)>=2 else sys.stdin
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        #N, R, P, S = int( f.next().strip() )
        N, R, P, S = map( int, f.next().strip().split() )
        print "Case #{0}: {1}".format( case, solve(N, R, P, S) )
        

if __name__ == "__main__":
    main()
