# -*- coding: utf-8 -*-
"""
/**********************************************************************************************
* Sometimes it is the people no one imagines anything of who do the things no one can imagine.*
*                                                                                             *
*                                    User: LLcoolNJ                                           *
***********************************************************************************************/
"""
import sys
from collections import deque
inp = sys.stdin.readline

def getInt():
    return int(inp().strip())
    
def getList():
    return map(int, inp().strip().split())

def getStr():
    return inp().strip()
    
T = getInt()

for cs in xrange(1, T+1):
    S = getStr()
    res = deque()
    res.append(S[0])
    for i in xrange(1, len(S)):
        if S[i] >= res[0]:
            res.appendleft(S[i])
        else:
            res.append(S[i])
    ans = ''.join(res)
    print "Case #%d: %s" %(cs, ans)
