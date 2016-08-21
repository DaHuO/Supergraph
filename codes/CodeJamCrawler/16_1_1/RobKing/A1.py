from sys import *


def getdigits(M):
    result = []
    while M >= 10:
        Temp = M
        M = M / 10
        result.append(Temp - 10 * M)
    result.append(M)
    return result


def solve(T, L):
    result = ''
    result += L[0]
    for i in range(1, len(L)):
        if L[i] >= result[0]:
            result = L[i] + result
            
        else:
            result = result + L[i]
    print "Case #%d: %s" %(T+1, result)

cases = int(raw_input())
for T in xrange(cases):
    L = raw_input()
    solve(T, L)
