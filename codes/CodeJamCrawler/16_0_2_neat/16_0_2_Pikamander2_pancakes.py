lineNum = 0
numCases = 0
finishedCases = []

with open('B-large.in') as f:
    for line in f:
        line = line.rstrip()
        lineNum += 1
        if (lineNum == 1): #The first line is the #of cases
            numCases = int(line)
        else:
            #print ("line is " + line)
            lastSign = line[0]
            numSignChanges = 0
            lengthOfLine = len(line)
            #print('length of line is ' + str(lengthOfLine))
            for i in range(lengthOfLine):
                if (line[i] != lastSign): #1 sign change = one pancake flip
                    #print("sign change! changing " + lastSign + " to " + line[i])
                    numSignChanges += 1
                    lastSign = line[i]
                #if the last sign in negative, add one pancake flip
                if (i == lengthOfLine - 1 and line[i] == "-"):
                    #print("adding one!")
                    numSignChanges += 1
            finishedCases.append(numSignChanges)
                
                        

outputFile = open('pancakes.out', 'w')
for i in range(len(finishedCases)):
    if (i != 0):
        outputFile.write('\n') #spacing
    outputFile.write("Case #" + str(i+1) + ": " + str(finishedCases[i]))
outputFile.close()
print("done!")
