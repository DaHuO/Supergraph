#CodeJam pancake problem
import csv

#import data from test file in the form [[[],[]],[[],[]].... with [[],[]] being one test case
with open('B-large.in') as csvfile:
    testCase = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    rowNum = 0
    inputText = []
    #swapCount = []
    
    for row in testCase:
        #row = [str(i) for i in row]
        if rowNum == 0:
            numTestCases = int(row[0])
        else:
            inputText.append(row)
        rowNum = rowNum + 1

    #find the minimum time to eat pancakes
    for caseNum in range(0,numTestCases):
        lastLet = ''
        swapCount = 0
        #swapCount.append(0)
        for i in range(0,len(inputText[caseNum][0])):
             if inputText[caseNum][0][i] != lastLet:   
                swapCount = swapCount + 1
                lastLet = inputText[caseNum][0][i]
        if inputText[caseNum][0][len(inputText[caseNum][0])-1] == "+":
            swapCount = swapCount-1
        print "Case #" + str(caseNum+1) + ": " + str(swapCount)
#        maxTime = max(inputText[caseNum][1])
 #       testCounter = 0
 #       casePlates = sorted(inputText[caseNum][1])
 #       improveTime = [0]
#
#        if len(casePlates) > 1:
#            if casePlates[-1]/casePlates[-2]>=3:
#                improveTime.append(casePlates[-1]*2/3 - 2)
#                tempVal=casePlates[-1]
#                casePlates.append(casePlates[-1]*2/3)
#                casePlates[-2]= tempVal*2/3
#                testCounter = testCounter+1
#                casePlates = sorted(casePlates)

#                while casePlates[-1]/2 -1 > (max(improveTime)-improveTime[testCounter]) and casePlates[-1] > 3:
#                    if casePlates[-2] >= casePlates[-1]/2 + casePlates[-1] % 2:
#                        improveTime.append(improveTime[-1] + casePlates[-1] - casePlates[-2] - 1)
#                    else:
#                        improveTime.append(improveTime[-1] + casePlates[-1]/2 - 1)
#                    
#                    tempVal=casePlates[-1]
#                    casePlates.append(casePlates[-1]/2)
#                    casePlates[-2]= tempVal/2 + tempVal % 2
#                    testCounter = testCounter+1
#                    casePlates = sorted(casePlates)

#            elif len(casePlates)>2 and (casePlates[-1]/casePlates[-2]>=1.5 and casePlates[-1]/casePlates[-3]>=3):
#                improveTime.append(casePlates[-1]*2/3-2)
#                tempVal=casePlates[-1]
#                casePlates.append(casePlates[-1]*2/3)
#                casePlates[-2]= tempVal*2/3
#                testCounter = testCounter+1
#                casePlates = sorted(casePlates)

#                while casePlates[-1]/2 -1 > (max(improveTime)-improveTime[testCounter]) and casePlates[-1] > 3:
#                    if casePlates[-2] >= casePlates[-1]/2 + casePlates[-1] % 2:
#                        improveTime.append(improveTime[-1] + casePlates[-1] - casePlates[-2] - 1)
#                    else:
#                        improveTime.append(improveTime[-1] + casePlates[-1]/2 - 1)
#                    
#                    tempVal=casePlates[-1]
#                    casePlates.append(casePlates[-1]/2)
#                    casePlates[-2]= tempVal/2 + tempVal % 2
#                    testCounter = testCounter+1
#                    casePlates = sorted(casePlates)

#            elif len(casePlates)==2 and (float(casePlates[-1])/float(casePlates[-2])>=1.5) and casePlates[-1]/casePlates[-2]< 2:
#                improveTime.append(casePlates[-1]*1/3)
#                tempVal=casePlates[-1]
#                casePlates.append(casePlates[-1]*2/3)
#                casePlates[-2]= tempVal*2/3
#                testCounter = testCounter+1
#                casePlates = sorted(casePlates)

#                while casePlates[-1]/2 -1 > (max(improveTime)-improveTime[testCounter]) and casePlates[-1] > 3:
#                    if casePlates[-2] >= casePlates[-1]/2 + casePlates[-1] % 2:
#                        improveTime.append(improveTime[-1] + casePlates[-1] - casePlates[-2] - 1)
#                    else:
#                        improveTime.append(improveTime[-1] + casePlates[-1]/2 - 1)
#                    
#                    tempVal=casePlates[-1]
#                    casePlates.append(casePlates[-1]/2)
#                    casePlates[-2]= tempVal/2 + tempVal % 2
#                    testCounter = testCounter+1
#                    casePlates = sorted(casePlates)

#            else:
#                while casePlates[-1]/2 -1 > (max(improveTime)-improveTime[testCounter]) and casePlates[-1] > 3:
#                    if casePlates[-2] >= casePlates[-1]/2 + casePlates[-1] % 2:
#                        improveTime.append(improveTime[-1] + casePlates[-1] - casePlates[-2] - 1)
#                    else:
#                        improveTime.append(improveTime[-1] + casePlates[-1]/2 - 1)
#                    
#                    tempVal=casePlates[-1]
#                    casePlates.append(casePlates[-1]/2)
#                    casePlates[-2]= tempVal/2 + tempVal % 2
#                    testCounter = testCounter+1
#                    casePlates = sorted(casePlates)

#        else:
#            if casePlates[0] == 1:
#                improveTime[0] = 0
#            elif casePlates[0]== 9:
#                improveTime[0] = 4
#            else:
#                improveTime[0] = maxTime - casePlates[0]/2 - 1 - casePlates[-1] % 2
#        print "Case #" + str(caseNum+1) + ": " + str(maxTime - max(improveTime))
#