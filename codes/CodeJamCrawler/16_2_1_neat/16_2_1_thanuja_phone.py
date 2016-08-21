'''
Created on Apr 30, 2016

@author: thanuja
'''

import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def removeChars(inputString, ALLLETTERS, numA):
    newString = inputString
    
    for c in ALLLETTERS:
        numC = newString.count(c)
        # remove c
        newString = newString.replace(c,"")
        str1 = c * (numC - numA)
        newString = newString + str1

    return newString

def processString(inputString, A, ALLLETTERS):
    numA = inputString.count(A)
    newString = removeChars(inputString, ALLLETTERS, numA)
    return (numA, newString)

def getDigits(inputString):

    digitsAll = ''
    # zeros
    # count z s
    # modify input string
    numDigits,newString = processString(inputString, 'Z', 'ZERO')
    str1 = '0' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'X', 'SIX')
    str1 = '6' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'G', 'EIGHT')
    str1 = '8' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'W', 'TWO')
    str1 = '2' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'S', 'SEVEN')
    str1 = '7' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'V', 'FIVE')
    str1 = '5' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'F', 'FOUR')
    str1 = '4' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'H', 'THREE')
    str1 = '3' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits,newString = processString(newString, 'O', 'ONE')
    str1 = '1' * numDigits
    digitsAll = digitsAll + str1
    
    numDigits = newString.count('I')
    str1 = '9' * numDigits
    digitsAll = digitsAll + str1
    
    digitsSorted = natural_sort(digitsAll)
    
    return digitsSorted

inputFileName = '../inputs/a_phone/A-large.in';
outputFileName = '../outputs/a_phone/test.out'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')

lines = f.readlines()
numTests = int(lines[0])

for i in range(1,numTests+1):
    inputString = lines[i]
    
    out = getDigits(inputString)
    str1 = 'Case #' + str(i) + ': ' + ''.join(out) + '\n'
    fout.write(str1)
    
f.close()
fout.close()

if __name__ == '__main__':
    pass


