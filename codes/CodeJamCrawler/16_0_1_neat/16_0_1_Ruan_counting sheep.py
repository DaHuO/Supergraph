# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 07:18:18 2016

@author: theronrp
"""

f = open('Alarge.in')
fo = open('output.out', 'w')

testCases = int(f.readline())
print testCases

for i in range(0,testCases):
    initialNumber = int(f.readline())
    if initialNumber == 0:
        print "Case #" + str(i + 1) + ": " + "INSOMNIA"
        fo.write("Case #" + str(i + 1) + ": " + "INSOMNIA\n")
        continue 
    
    #Initialize the variables
    asleep = False
    currentMul = 0
    digitsSeen = [0] * 10
    number = initialNumber
    while not asleep:
        currentMul += 1        
        number = currentMul * initialNumber
        
        #Get all the digits in the current number        
        div = number
        mod = 0
        tempNumber = number
        while div != 0:
            div = tempNumber / 10
            mod = tempNumber % 10
            digitsSeen[mod] += 1
            tempNumber = div
            
        #Test if she's asleep
        asleep = True
        for digit in digitsSeen:
            if digit == 0:
                asleep = False
                
    print "Case #" + str(i + 1) + ": " + str(number)
    fo.write("Case #" + str(i + 1) + ": " + str(number) + '\n')

f.close
fo.close            
        
    