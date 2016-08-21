#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2016 round 1 C
A
'''

dic = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def valid2(N, P):
    n = sum(P)
    P2 = P[:]
    if sum(P) <= 1:
        return ''
    Q = P[:]
    Q.sort(reverse=True)
    max1 = P.index(Q[0])
    P2[max1] = -1
    Q = P2[:]
    Q.sort(reverse=True)
    max2 = P2.index(Q[0])
    for i in range(N):
        if i == max1 or i == max2:
            if P[i] - 1 > (n - 2) / 2.0:
                return ''
        else:
            if P[i] > (n - 2) / 2.0:
                return ''
    else:
        P[max1] -= 1
        P[max2] -= 1
        return (dic[max1] + dic[max2])


def valid1(N, P):
    n = sum(P)
    Q = P[:]
    Q.sort(reverse=True)
    max1 = P.index(Q[0])
    for i in range(N):
        if i == max1:
            if P[i] - 1 > (n - 1) / 2.0:
                return ''
        else:
            if P[i] > (n - 1) / 2.0:
                return ''
    else:
        P[max1] -= 1
        return dic[max1]


def solution(N, P):
    ans = []
    while sum(P) > 0:
        v2 = valid2(N, P)
        if v2 != '':
            ans.append(v2)
        else:
            v1 = valid1(N, P)
            ans.append(v1)
    return ' '.join(ans)


T = int(raw_input())
for case_number in range(1, T + 1):
    N = int(raw_input())
    P = map(int, raw_input().split())
    print 'Case #%d: %s' % (case_number, solution(N, P))
