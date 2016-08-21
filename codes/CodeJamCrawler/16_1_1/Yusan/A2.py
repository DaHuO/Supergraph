#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2016 round 1 A
'''

def answer(S):
    ans = S[0]
    for i in range(1, len(S)):
        if S[i] + ans > ans + S[i]:
            ans = S[i] + ans
        else:
            ans = ans + S[i]
    return ans


T = int(raw_input())
for case_number in range(1, T + 1):
    S = raw_input().rstrip()
    print 'Case #%d: %s' % (case_number, answer(S))
