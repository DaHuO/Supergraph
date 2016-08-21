# Author:   Jurgen Nijland
# Date:     08-05-2016

import sys
import heapq
from var_dump import var_dump

caseCnt = 1
def printcase(val):
    global caseCnt
    print("Case #" + str(caseCnt) + ": " + val)
    caseCnt += 1

def stringToOrd(str):
    return list(map(ord, str.rstrip()))

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

numCases = int(sys.stdin.readline())
for i in range(0, numCases):
    ans = ""
    N = int(sys.stdin.readline())
    P = [int(x) for x in sys.stdin.readline().split(' ')]
    m = heapq.nlargest(2, range(len(P)), P.__getitem__)
    while (P[m[0]] > 0):
        if (P[m[0]] == P[m[1]] and (sum(P) <= 2 or P[m[0]] + P[m[1]] == sum(P))):
            P[m[0]] = P[m[0]] - 1
            P[m[1]] = P[m[1]] - 1
            ans += chr(ord('A') + m[0])
            ans += chr(ord('A') + m[1])
        else:
            P[m[0]] = P[m[0]] - 1
            ans += chr(ord('A') + m[0])
        m = heapq.nlargest(2, range(len(P)), P.__getitem__)
        ans += " "
    printcase(ans)
