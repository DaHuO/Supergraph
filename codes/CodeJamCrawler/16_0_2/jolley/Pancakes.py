# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:01:19 2016

@author: jo
"""

with open('input', 'r') as f:
    cases = 0
    case = 0
    with open('outputPan', 'w') as fo:
     for line in f:
        
        if line[0].isdigit():
            cases = int(line)
            #print(line)
        else:
            case +=1
            last = True
            flips = 0
            
            for c in xrange(len(line)):
                positive = True
                if line[c] == '-':
                    positive = False
                if c == 0:
                    last = positive
                else:
                    if positive != last:
                        flips +=1
                    if c == (len(line)-1):
                        if positive != True:
                            flips += 1
                        fo.write('Case #' + str(case) + ': ' + str(flips) + '\n')
                    last = positive
                    
                