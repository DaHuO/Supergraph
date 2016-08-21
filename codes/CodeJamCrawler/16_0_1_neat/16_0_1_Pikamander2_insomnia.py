lineNum = 0
numCases = 0
numberToTest = -1
neededNumbers = [0,1,2,3,4,5,6,7,8,9]
finishedNumbers = [] #Insomnia = -1

with open('A-large.in') as f:
    for line in f:
        lineNum += 1
        if (lineNum == 1): #The first line is the #of cases
            numCases = int(line)
        else:
            seenNumbers = []
            numberToTest = int(line)
            counter = 0
            numberTimesCounter = 0
            #print(numberToTest)
            if (numberToTest == 0):
                finishedNumbers.append("INSOMNIA")
                continue
            while(len(seenNumbers) < 10):
                counter += 1
                numberTimesCounter = numberToTest * counter
                numAsString = str(numberTimesCounter) #ex: "534"
                for i in range(len(numAsString)):
                    if (numAsString[i] not in seenNumbers):
                        seenNumbers.append(numAsString[i])
                #print(seenNumbers)
            finishedNumbers.append(numberTimesCounter)
                        

outputFile = open('practice.out', 'w')
for i in range(len(finishedNumbers)):
    #print(str(finishedNumbers[i]))
    if (i != 0):
        outputFile.write('\n') #spacing
    outputFile.write("Case #" + str(i+1) + ": " + str(finishedNumbers[i]))
outputFile.close()
print("done!")
            
            
##            numberToTest = line
##            splitLine = line.split()
##            if (len(splitLine) == 1): #New case
##                calculate(currentCase) #Calculate the last case before starting a new one
##                caseNum += 1
##                currentCase = []
##            else: #Another wire
##                currentCase.append([float(splitLine[0]),float(splitLine[1])])


