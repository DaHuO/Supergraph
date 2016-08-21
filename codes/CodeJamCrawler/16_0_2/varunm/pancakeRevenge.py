'''
Created on 09-Apr-2016

@author: varunm
'''
def checkPancake(inputString):
    for x in inputString:
        if(x == '-'):
            return False
            break
    return True

    
def flipPancake(caseNo, inputString, counter):
    originalStringLen = len(inputString)
    if(checkPancake(inputString)):
        print "Case #"+str(caseNo)+":",counter
    else:
        #get top y of the same sign
        #flip pancakes
        #increment counter
        #recurse
        #print "original length ",originalStringLen
        testString = ""
        checkVariable = inputString[:1]        
        for i in inputString:
            if(i == checkVariable):
                testString += i
            else:
                break
        #print testString
        currStringLen = len(testString)
        subStringLeft = inputString[:currStringLen]
        subStringRight = inputString[currStringLen:]
        #print "Current Length",currStringLen
        #print "left ",subStringLeft
        #print "right ",subStringRight
        if(checkVariable=='-'):
            replacedString = subStringLeft.replace('-','+')
        else:
            replacedString = subStringLeft.replace('+','-')
        newString = replacedString+subStringRight
        flipPancake(caseNo,newString, counter+1)

def fileRead():
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])  
    for i in range(1, noTestCases+1):
        #print "Testing #",i," : ",lineList[i]        
        flipPancake(i,lineList[i],0)

def main():
    fileRead()
    
if __name__ == "__main__":
    main()