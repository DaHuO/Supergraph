# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 07:28:15 2016

@author: madushan
"""
from collections import Counter

nTestCases = int(raw_input())


for test in range(nTestCases):
    counter = Counter('')
    count = [0]
    number = int(raw_input())
    iteration = 0
    output = 0
    while count[-1] != 10:
        iteration += 1
        #print "n", iteration * number
        counter.update(str(iteration * number))
        if len(count) > 10 and count[-1] - count[1] < 1:
            output = "INSOMNIA"
            break
        count.append(len(counter.keys()))
        output = number * iteration
    print "Case #{}:".format(test + 1), output
    #print counter