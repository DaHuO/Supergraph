'''
Created on Apr 9, 2016

@author: thanuja
'''

def removeCharFromString(inputString,i):
    newstr = inputString[:i] + inputString[(i+1):]
    return newstr

def removeConsecutiveDuplicates(inputString):
    if(len(inputString)<2):
        return inputString
    else:
        newString = []
        newString.append(inputString[0])
        for i in range(len(inputString)-1):
            j=i+1
            if(j<=len(inputString)):  
                if( not (inputString[i] is inputString[j]) ):
                    newString.append(inputString[j])
    return ''.join(newString)

def getOperations(inputPattern):
    inputPattern = removeConsecutiveDuplicates(inputPattern)
    # remove last element if equal to +
    if(inputPattern[len(inputPattern)-1] is '+'):
        inputPattern = inputPattern[:-1]
    numOperations = len(inputPattern)
    return numOperations
    
    