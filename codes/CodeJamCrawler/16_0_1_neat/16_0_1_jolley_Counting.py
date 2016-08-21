# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 08:54:46 2016

@author: jo
"""
        

with open('input', 'r') as f:
    cases = 0
    case = 0
    with open('outputCount', 'w') as fo:
     for line in f: 
        if case == 0:
            cases = int(line)
            case = 1            
        else:
            fo.write('Case #' + str(case) + ': ')
            print('Case: ' + str(case))
            case +=1
            N = int(line)
            print(N)
            if N == 0:
                fo.write('INSOMNIA\n')
                continue
            allNumbers = False
            numbers = [False]*10
            x = 10**20
            i = 1
            while True:
                for n in str(N*i):
                    numbers[int(n)] = True   
                allTrue = True
                for digit in xrange(len(numbers)):
                    if(numbers[digit] == False):
                        allTrue = False
                        break
                if allTrue: 
                    fo.write(str(i*N) + '\n')
                    break
                i += 1
                if(i>10**1000):
                    fo.write('INSOMNIA\n')
                    break