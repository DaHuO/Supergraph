import sys

inputStrings = open('A-large.in', 'r').read().splitlines()
caseNum = int(inputStrings[0])
outString = ""

for case in range(0,caseNum):
    word = inputStrings[case+1]
    lastword = word[0];
    for i in range(1, len(word)):
        if(word[i] >= lastword[0]):
            lastword = word[i] + lastword
        else:
            lastword += word[i]
    outString += "Case #" + str(case+1) + ": " + lastword + "\n"

fileOut = open('A-large.out', 'w')
fileOut.write(outString)
fileOut.close()