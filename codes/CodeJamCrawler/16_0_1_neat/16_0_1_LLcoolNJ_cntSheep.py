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

for cs in xrange(1, T+1):
    cnt = [False]*10
    N = getInt()    
    if N == 0:
        print "Case #%d: INSOMNIA" %(cs)
        continue
    num = 1
    while True:
        ans = num*N
        #print ans
        for i in map(int, list(str(ans))):
            cnt[i] = True
        fl = True
        for i in cnt:
            fl = fl&i
        if fl:
            break
        num += 1
    print "Case #%d: %s" %(cs, num*N)