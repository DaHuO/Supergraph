#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2016 qualification round
D: Fractiles
'''


def answer(K, C, S):
    '''
    '''

    ans = []
    for s in range(S):
        ans.append(1 + s * K ** (C - 1))
    return ' '.join(map(str, ans))


T = int(raw_input())
for case_number in range(1, T + 1):
    K, C, S = map(int, raw_input().split())
    print 'Case #%d: %s' % (case_number, answer(K, C, S))
