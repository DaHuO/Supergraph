lineNum = 0
numCases = 0

outputFile = open('practice.out', 'w')

with open('A-large.in') as f:
    for line in f:
        line = line.rstrip()
        lineNum += 1
        if (lineNum == 1): #The first line is the #of cases
            numCases = int(line)
        else:
            word = ""
            for i in range(len(line)):
                if (word == ""):
                    word += line[i]
                else:
                    if (word[0] > line[i]):
                        word = word + line[i]
                    else:
                        word = line[i] + word
            if (lineNum != 2):
                outputFile.write("\n")
            outputFile.write("Case #" + str(lineNum-1) + ": " +word)
outputFile.close()
