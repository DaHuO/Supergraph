# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:01:54 2016

@author: theronrp
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:18:51 2016

@author: theronrp
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:54:59 2016

@author: theronrp
"""

f = open('a-large.in')
fo = open('output.out', 'w')

testCases = int(f.readline())
print testCases

numberNames = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def find_number(inputStringList, number):
    
    contains_letter = [False]*len(number)
    already_seen = [False]*len(inputStringList)
    
    for i, number_item in enumerate(number):
        for count in range(0, len(inputStringList)):
            if (inputStringList[count] == number_item) and (already_seen[count] == False):
                contains_letter[i] = True
                already_seen[count] = True
                break
                
    if sum(contains_letter) == len(number):
        return True
    else:
        return False
        
def remove_number(inputStringList, number):
    for number_item in number:
        for i in range(0,len(inputStringList)):
            if number_item == inputStringList[i]:
                del inputStringList[i]
                break
    
    return

for i in range(0,testCases):
    
    mixedNumber = list(str(f.readline()).rstrip('\n'))
    original = mixedNumber[:]
    startNumber = 0
    freq = [0]*10
    telephoneNumber = []
    
    #Count the 0's
    zerocount = 0
    for letter in mixedNumber:
        if letter == 'Z':
            zerocount += 1
            telephoneNumber.append(0)
            
    for j in range(0,zerocount):
        remove_number(mixedNumber, list('ZERO'))
        
    #Count the 2's
    zerocount = 0
    for letter in mixedNumber:
        if letter == 'W':
            zerocount += 1
            telephoneNumber.append(2)
            
    for j in range(0,zerocount):
        remove_number(mixedNumber, list('TWO'))
        
        
    #Count the 4's
    zerocount = 0
    for letter in mixedNumber:
        if letter == 'U':
            zerocount += 1
            telephoneNumber.append(4)
            
    for j in range(0,zerocount):
        remove_number(mixedNumber, list('FOUR'))
        
    #Count the 6's
    zerocount = 0
    for letter in mixedNumber:
        if letter == 'X':
            zerocount += 1
            telephoneNumber.append(6)
            
    for j in range(0,zerocount):
        remove_number(mixedNumber, list('SIX'))
        
   
        
    #Count the 8's
    zerocount = 0
    for letter in mixedNumber:
        if letter == 'G':
            zerocount += 1
            telephoneNumber.append(8)
            
    for j in range(0,zerocount):
        remove_number(mixedNumber, list('EIGHT'))
    
    remaining = [1,3,5,7,9]    
    
    if len(mixedNumber) == 0:
        doneWithProblem = True
    else:
        doneWithProblem = False
    while not doneWithProblem:
        doneWithNumber = False
        
        for number in remaining:
            doneWithNumber = False
            while not doneWithNumber:        
            #Does is contain the first number?
                letters = list(numberNames[number])
                
                if find_number(mixedNumber, letters):
                    pass
                    telephoneNumber.append((number))
                    remove_number(mixedNumber, letters)
                    #freq[number] += 1
                else:
                    doneWithNumber= True
            
            if len(mixedNumber) == 0:
                doneWithProblem = True
                break
            
    if len(mixedNumber) != 0:
        print "ERROR!!!"
        
    telephoneNumber.sort()
        
    testlen = 0
    for tel in telephoneNumber:
        testlen += len (numberNames[tel])
        
    print i+1
    print len(original)
    print testlen
    if len(original) != testlen :
        print "ERROR!!!"
    print 
                
    fo.write('Case #' + str(i+1) + ': ' + ''.join(map(str,telephoneNumber)) + '\n')
    print 'Case #' + str(i+1) + ': ' + ''.join(map(str,telephoneNumber)) + '\n'
    
f.close()
fo.close()