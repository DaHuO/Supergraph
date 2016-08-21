# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 03:16:50 2016

@author: theronrp
"""

f = open('large.in')
fo = open('output.out', 'w')

testCases = int(f.readline())
print testCases

for i in range(0,testCases):
    letters = f.readline()
    letters = list(letters.rstrip())
    lastword = str(letters[0])
    first_letter = letters[0]
        
    for l in range(1, len(letters)):
        if letters[l] >= first_letter:
            lastword = str(letters[l]) + lastword
        else:
            lastword =  lastword + str(letters[l])
        first_letter = lastword[0]
    print lastword
    fo.write('Case #' + str(i+1) + ': ' + lastword + '\n')
    
f.close()
fo.close()