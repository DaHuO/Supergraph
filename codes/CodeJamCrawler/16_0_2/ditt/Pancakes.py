# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:25:53 2016

@author: Dittaya Wanvarie
"""

def flip(stack, flipIndex):
    part = stack[0:flipIndex]
    part.reverse()
    for i in range(flipIndex):
        if part[i] == '+':
            part[i] = '-'
        else:
            part[i] = '+'
    return part+stack[flipIndex:]

fout = open('B-large.out','w')
with open('B-large.in') as f:
    nCases = int(f.readline())
    case = 1
    for line in f:
        line = line.strip()
        stack = list(line)

        flipIndex = 1
        start = 0
        count = 0
        while start < len(stack):
            while flipIndex < len(stack) and stack[start] == stack[flipIndex]:
                flipIndex += 1
            if flipIndex < len(stack):
                stack = flip(stack, flipIndex)
                count += 1
            elif stack[start] == '-':
                stack = flip(stack, flipIndex)
                count += 1
            start = flipIndex

        print('Case #'+str(case)+': '+str(count), file=fout)
#        print('Case #'+str(case)+': '+str(count))
        case += 1
fout.flush()
fout.close()