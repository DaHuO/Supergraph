# -*- coding: utf-8 -*-
"""
/**********************************************************************************************
* Sometimes it is the people no one imagines anything of who do the things no one can imagine.*
*                                                                                             *
*                                    User: LLcoolNJ                                           *
***********************************************************************************************/
"""
import sys
inp = sys.stdin.readline

def getInt():
    return int(inp().strip())
    
def getList():
    return map(int, inp().strip().split())

def getStr():
    return inp().strip()
    
    
T = getInt()

out = {'+' : '-', '-' : '+'}
for cs in xrange(1, T+1):
    S = list(getStr())
    SLen = len(S)
    moves = 0
    while True:
        i = 0
        while i < SLen-1:
            if S[i] != S[i+1]:
                break
            i += 1
        if i == SLen-1 and S[0] == '+':
            break
        else:
            ind = 0
            while ind < i+1:
                S[ind] = out[S[ind]]
                ind += 1
        moves += 1
    ans = moves
    print "Case #%d: %s" %(cs, ans)