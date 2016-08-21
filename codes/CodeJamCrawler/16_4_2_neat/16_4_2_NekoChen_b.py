import sys, numpy as np
from itertools import combinations, permutations
from operator import itemgetter
from collections import deque, defaultdict
import heapq, random

def solve( N, K, P ):
    cachep, cacheq = {}, {}
    for i in combinations( range(N), K/2 ):
        #print itemgetter(*i)(P)
        pp = itemgetter(*i)(P) if len(i)>1 else [itemgetter(*i)(P)]
        cachep[i] = reduce( lambda a,b:a*b, pp )
        cacheq[i] = reduce( lambda a,b:a*(1.0-b), pp, 1.0 )
    def tie(i):
        s = 0.0
        for j in combinations( i, K/2 ):
            k = tuple( sorted(( set(i).difference(j) )) )
            s += cachep[j] * cacheq[k]
            s += cachep[k] * cacheq[j]
        return s
    
    ptie = [ tie(i) for i in combinations( range(N), K ) ]
    return max(ptie)/2
        


def main():
    f = open( sys.argv[1] ) if len(sys.argv)>=2 else sys.stdin
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        #N, R, P, S = int( f.next().strip() )
        N, K = map( int, f.next().strip().split() )
        P = map( float, f.next().strip().split() )
        #a, b = solve(N, R, P, S), solve2(N, R, P, S)
        #if a != b:
        #    print "!!!!", a, b
        print "Case #{0}: {1}".format( case, solve(N, K, P) )
        

def main2():
    pass

if __name__ == "__main__":
    if len(sys.argv)<2:
        main2()
    else:
        main()
