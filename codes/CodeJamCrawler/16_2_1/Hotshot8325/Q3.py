#CodeJam
import csv

#import data from test file in the form [[[],[]],[[],[]].... with [[],[]] being one test case
with open('a-large.in') as csvfile:
    testCase = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    rowNum = 0
    inputText = []
    for row in testCase:
        if rowNum == 0:
            numTestCases = int(row[0])
        else:
            inputText.append(row)
        rowNum = rowNum + 1
    
    for caseNum in range(0,numTestCases):
        letterCount = [0]*10
        phoneNumbers = [0]*10
        phoneNumber = ""
        for letter in inputText[caseNum][0]:
            if letter == "Z":
                letterCount[0]+=1
            if letter == "O":
                letterCount[1]+=1
            if letter == "W":
                letterCount[2]+=1
            if letter == "H":
                letterCount[3]+=1
            if letter == "R":
                letterCount[4]+=1
            if letter == "F":
                letterCount[5]+=1
            if letter == "X":
                letterCount[6]+=1
            if letter == "V":
                letterCount[7]+=1
            if letter == "G":
                letterCount[8]+=1
            if letter == "N":
                letterCount[9]+=1
        phoneNumbers[0] = letterCount[0]
        phoneNumbers[2] = letterCount[2]
        phoneNumbers[6] = letterCount[6]
        phoneNumbers[8] = letterCount[8]
        phoneNumbers[3] = letterCount[3]-phoneNumbers[8]
        phoneNumbers[4] = letterCount[4]-phoneNumbers[0]-phoneNumbers[3]
        phoneNumbers[5] = letterCount[5]-phoneNumbers[4]
        phoneNumbers[7] = letterCount[7]-phoneNumbers[5]
        phoneNumbers[1] = letterCount[1]-phoneNumbers[0]-phoneNumbers[2]-phoneNumbers[4]
        phoneNumbers[9] = (letterCount[9]-phoneNumbers[7]-phoneNumbers[1])/2
        for j in range(0,10):
            for k in range(0,phoneNumbers[j]):
                phoneNumber = phoneNumber + str(j)


        print "Case #" + str(caseNum+1) + ": " + ' ' + phoneNumber
        #print "Case #" + str(caseNum) + " " + ' '.join(List to print)
    
 
   
    
    