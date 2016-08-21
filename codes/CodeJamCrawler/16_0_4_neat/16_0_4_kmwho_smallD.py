#! /usr/bin/python3
# kmwho

from __future__ import print_function

def solvecase():
    K,C,S  = map(int, input().strip().split() )
    Smin   = (K+C-1)//C
    if S < Smin:
        return "IMPOSSIBLE"
    kpow   = [ K**i  for i in range(C+1) ]
    nums   = []
    for j in range( min(S,Smin) ):
        nums.append( tuple( sorted( (C*j + i) % K for i in range(C) ) ) )
    vals   = [  str( 1 + sum( num[i]*kpow[C-i-1] for i in range(C) )) for num in nums ]
    #print( nums )
    return " ".join( vals )

def solve():
    T  = int(input())
    for t in range(T):
        res = solvecase()
        print( "Case #" + str(t+1) + ": " + str(res) )

def main():
	solve()


main()
