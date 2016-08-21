#! /usr/bin/python
# kmwho
# CodeJam 2016  1C

from __future__ import print_function


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def step(senate):
    max1,max2 = (0,0),(0,0)
    q1,q2  = "", ""
    tot  = 0
    N    = len(senate)
    
    for i in range(N):
        si   = senate[i]
        tot += si
        if si >= max1[0]:
            max1,max2 = (si,i) , max1
        elif si >= max2[0]:
            max2 = (si,i)
    if max1[0] > max2[0]+1:
        p1 = max1[1]
        p2 = p1
    else:
        p1 = max1[1]
        p2 = max2[1]

    if tot <= 0:
        return ""
    
    #print( "senate ", senate)
    #print( "p1p2 ", tot, p1,p2)
    
    if tot == 3:
        senate[p1] -= 1
        return alphabet[p1]


    if senate[p1] > 0:
        senate[p1] -= 1
        q1 = alphabet[p1]

    if senate[p2] > 0 and 2*(senate[p2]-1) <= (tot-2):
        senate[p2] -= 1
        q2 = alphabet[p2]
    
    return q1 + q2

def solvecase():
    N        = int(input())
    senate   = list(map(int, input().strip().split() ))
    tot      = sum(senate)
    plan     = []
    
    while True:
        s = step(senate)
        if s:
            plan.append(s)
        else:
            break

    return " ".join(plan)

def solve():
    T  = int(input())
    for t in range(1,T+1):
        res = solvecase()
        print( "Case #" + str(t) + ": " + str(res) )

def main():
	solve()


main()
