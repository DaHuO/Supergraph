from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

dic = {}

dic[2] = 'TWO'
dic[6] = 'SIX'
dic[8] = 'EIGHT'
dic[7] = 'SEVEN'
dic[5] = 'FIVE'
dic[4] = 'FOUR'

dic[0] = 'ZERO'
dic[1] = 'ONE'
dic[3] = 'THREE'
dic[9] = 'NINE'


def recover(s):

    ans = []

    while 'Z' in s:
        ans.append(0)
        for c in dic[0]:
            s = s.replace(c, '', 1)

    while 'W' in s:
        ans.append(2)
        for c in dic[2]:
            s = s.replace(c, '', 1)

    while 'X' in s:
            ans.append(6)
            for c in dic[6]:
                s = s.replace(c, '', 1)

    while 'G' in s:
            ans.append(8)
            for c in dic[8]:
                s = s.replace(c, '', 1)

    while 'S' in s:
            ans.append(7)
            for c in dic[7]:
                s = s.replace(c, '', 1)

    while 'V' in s:
            ans.append(5)
            for c in dic[5]:
                s = s.replace(c, '', 1)

    while 'F' in s:
            ans.append(4)
            for c in dic[4]:
                s = s.replace(c, '', 1)

    while 'O' in s:
            ans.append(1)
            for c in dic[1]:
                s = s.replace(c, '', 1)

    while 'T' in s:
            ans.append(3)
            for c in dic[3]:
                s = s.replace(c, '', 1)

    while 'N' in s:
            ans.append(9)
            for c in dic[9]:
                s = s.replace(c, '', 1)

    ans.sort()
    return "".join(map(str, ans))

T = int(stdin.readline())

for i in range(1,T+1):

    s, = stdin.readline().split()
    
    print "Case #" + str(i) + ":", 

    print recover(s)