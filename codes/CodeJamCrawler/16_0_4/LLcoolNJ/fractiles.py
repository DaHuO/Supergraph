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
#### Foo Small Dataset
for cs in xrange(1, T+1):
    K, C, S = getList()
    if S < K:
        print "Case #%d: IMPOSSIBLE" %(cs)
        continue
    if S%2 == 0:
        ans = map(str, range(1, S/2 + 1))
        ans = ans + map(str, range(K**C - S/2 + 1, K**C + 1))
    else:
        ans = map(str, range(1, S/2 + 1))
        ans = ans + [str(K**C / 2 + 1)]
        ans = ans + map(str, range(K**C - S/2 + 1, K**C + 1))        
    ans = ' '.join(ans)
    print "Case #%d: %s" %(cs, ans)