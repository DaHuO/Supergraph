#CodeJam coin problem
import csv

#import data from test file in the form [[[],[]],[[],[]].... with [[],[]] being one test case
with open('B-small-attempt0.in') as csvfile:
    testCase = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    rowNum = 0
    inputText = []
    successValues = []
    successFactors = []
    
    for row in testCase:
        if rowNum == 0:
            numTestCases = int(row[0])
        else:
            inputText.append(row)
        rowNum = rowNum + 1
    
    numFound = 0
    numValue = int(str(10**(int(inputText[0][0])-1)+1),2)
   
    
    #for i in range(0,8):
    #    print int(str(bin(numValue))[2:],i+2)
    
    print "Case #1:"
    factorValues = []
    numCount = 0
    totalCount = 0
    while totalCount < int(inputText[0][1]) and numValue < 2**(int(inputText[0][0])):
        prime = [0,0,0,0,0,0,0,0,0]
        cycCount = 0
        numCount = 0
        primaryFactors = []
        while cycCount < 9 and numCount < 1:
            factorTest = int(str(bin(numValue))[2:],cycCount+2)
            factorForNext = 2
            jCycCount = 2
            factorTrue = 0
            while jCycCount < int(factorTest**0.5) + 1:
                #print factorTest,jCycCount,factorTest%jCycCount
                if factorTest%jCycCount == 0:
                    prime[cycCount] = 1
                    primaryFactors.append(jCycCount)
                    successTest = factorTest
                    factorTest = 1
                    break
                jCycCount = jCycCount + 1
            if prime[cycCount]==0:
                break    
            
            if prime == [1,1,1,1,1,1,1,1,1]:
                print successTest, primaryFactors[0], primaryFactors[1], primaryFactors[2], primaryFactors[3], primaryFactors[4], primaryFactors[5], primaryFactors[6], primaryFactors[7], primaryFactors[8]
                #successValues.append(successTest)
                numCount = numCount+1
                #successFactors.append(primaryFactors)
                totalCount = totalCount + 1
            cycCount = cycCount + 1
        numValue = numValue + 2
    
   
 