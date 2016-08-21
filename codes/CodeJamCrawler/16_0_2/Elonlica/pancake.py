# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:04:58 2016

@author: elon
"""
for i in range(int(raw_input())):
    pancake = raw_input()
    pancake += '+'
    last_pan = pancake[0]
    result = 0
    for j in pancake[1:]:
        if last_pan != j:
            result += 1
            last_pan = j
    print "Case #%d: %d"  % (i+1, result)