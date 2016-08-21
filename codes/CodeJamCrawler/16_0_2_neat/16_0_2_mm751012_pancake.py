# coding: utf-8

import sys
import re

rl = lambda: sys.stdin.readline().strip()
plus = re.compile(r'¥+$')
minus = re.compile(r'^[-]+')


for case in range(int(rl())):
    S = list(rl())
    case = "Case #%d:" % (case+1)

    n = 0
    while True:
        #print case, '1',S
        # remove right-end '+'s
        while len(S)>0 and S[-1]=='+':
            S = S[:-1]
        #print case, '2',S

        if len(S)==0:
            print case, n
            break

        # flip left-end '+'s
        if S[0]=='+':
            n += 1
            i = 0
            while i<len(S) and S[i]=='+':
                S[i] = '-'
                i += 1
        #print case, '3', S

        # flip
        S.reverse()
        for i in range(len(S)):
            if S[i]=='+':
                S[i] = '-'
            else:
                S[i] = '+'
        n += 1
        #print case, '4', S

        #break