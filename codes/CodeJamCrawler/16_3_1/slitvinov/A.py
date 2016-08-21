#!/usr/bin/python

from collections import deque
import heapq

def ir():
    return int(raw_input())

def ia():
    line = raw_input()
    line = line.split()
    return map(int, line)

def val(e):
    return -e[0]

def idx(e):
    return e[1]

def ch(i):
    return chr( ord('A') + i)

def ev(A, B):
    ans = ''
    iA = idx(A)
    cA = ch(iA)
    ans = ans + cA
    if B!=None:
        iB = idx(B)
        cB = ch(iB)
        ans = ans + cB
    return ans

def hsum(h):
    return sum([-e for e, i in h])
        
def solve():
    n = ir()
    h = ia()
    h = [-e for e in h]
    h = [(e, i) for i, e in enumerate(h)]
    heapq.heapify(h)

    ans = ''
    while True:
        n = hsum(h)
        if n==0: break
        if n==1:
            p1 = heapq.heappop(h)
            ans = ans + ev(p1, None) + ' '
            break
        if n==2:
            p1 = heapq.heappop(h)
            p2 = heapq.heappop(h)            
            ans = ans + ev(p1, p2) + ' '
            break

        p1 = heapq.heappop(h)
        p1 = -(val(p1) - 1), idx(p1)
        heapq.heappush(h, p1)

        p2 = heapq.heappop(h)
        p3 = heapq.heappop(h) ; heapq.heappush(h, p3)
        ok = True

        if 2*val(p3)>n-2:
            ok = False
            heapq.heappush(h, p2)
        else:
            p2 = -(val(p2) - 1), idx(p2)
            heapq.heappush(h, p2)

        if ok:
            ans = ans + ev(p1, p2) + ' '
        else:
            ans = ans + ev(p1, None) + ' '

    ans = ans.strip()
    return ans

T = ir()
for i in range(T):
    print "Case #%d: %s" % (i+1, solve())
