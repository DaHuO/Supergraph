# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:59:27 2016

@author: Dittaya Wanvarie
"""

num = dict()
num[0] = list('ZERO')
num[1] = list('ONE')
num[2] = list('TWO')
num[3] = list('THREE')
num[4] = list('FOUR')
num[5] = list('FIVE')
num[6] = list('SIX')
num[7] = list('SEVEN')
num[8] = list('EIGHT')
num[9] = list('NINE')

fout = open('A-large.out', 'w')
with open('A-large.in') as f:
    nCases = int(f.readline())
    for case in range(nCases):
        line = f.readline().strip()
        ans = ''
        while 'Z' in line:
            ans += '0'
            for c in num[0]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'W' in line:
            ans += '2'
            for c in num[2]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'U' in line:
            ans += '4'
            for c in num[4]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'O' in line:
            ans += '1'
            for c in num[1]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'R' in line:
            ans += '3'
            for c in num[3]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'F' in line:
            ans += '5'
            for c in num[5]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'X' in line:
            ans += '6'
            for c in num[6]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'S' in line:
            ans += '7'
            for c in num[7]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'G' in line:
            ans += '8'
            for c in num[8]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        while 'N' in line:
            ans += '9'
            for c in num[9]:
                key = line.find(c)
                line = line[0:key]+line[key+1:]
        ans = list(ans)
        ans.sort()
        print('Case #'+str(case+1)+': '+''.join(ans), file=fout)

fout.flush()
fout.close()