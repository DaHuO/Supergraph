# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:54:55 2016

@author: elon
"""


for i in range(int(raw_input())):
    number = int(raw_input())
    result = ""
    num_left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = 0
    if number == 0:
        result = "INSOMNIA"
    else:
        while True:
            #print number*turn
            if len(num_left) == 0:
                result = str(number*turn)
                break
            turn += 1
            num_split = str(number*turn)
            #print num_split
            for n in num_split:
                n = int(n)
                if n in num_left:
                    num_left.remove(n)
                    #print num_left
            if turn > 101:
                result = "INSOMNIA"
                break
            
            
        
    print "Case #" + str(i+1) + ": " + result
    