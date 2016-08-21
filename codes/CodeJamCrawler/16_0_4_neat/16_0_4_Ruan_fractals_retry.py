# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 18:11:50 2016

@author: theronrp
"""

f = open('input2.in')
fo = open('output.out', 'w')

testCases = int(f.readline())
print testCases

for i in range(0, testCases):
    (K, C, S) = map(int, (f.readline()).split(' '))
    outputLine = 'Case #' + str(i + 1) + ": "
    for j in range(1, K + 1):
        outputLine += str(j) + " "
    outputLine += '\n'
    print outputLine
    fo.write(outputLine)
    
f.close()
fo.close()