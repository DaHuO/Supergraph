#reading input
f = open('B-large.in','r')
out = open ('out','w')


#Helpers
def writeOut(case,value):
    output = "Case #" + str(case+1) + ": " + str(value)
    print output
    out.write(output + '\n')

def flipStack(index,case):
    newCase = ''
    for i in range(0,len(case)):
        if(i <= index):
            if(case[i] == '-'):
                newCase += '+'
            else:
                newCase += '-'
        else:
            newCase += case[i]

    return newCase

#Read number of cases
numCases = int(f.readline())
numSteps = 0

for i in range(0,numCases):
    lastBlank = -1
    case =f.readline().strip('\n')
    allHappy = False
    numSteps = 0
    while(not allHappy):
        lastBlank = -1
        for j in range(0,len(case)):
            if(case[j] == "-"):
                lastBlank = j
        if(lastBlank == -1):
            allHappy = True
        else:
            case = flipStack(lastBlank,case)
            numSteps +=1

    writeOut(i,numSteps)







