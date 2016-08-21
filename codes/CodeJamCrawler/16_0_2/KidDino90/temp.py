

f = open ('B-large.in', 'r')


def readInput ():
    listLine = f.read ().splitlines ()        
    stage1 (listLine)

def stage1 (listLine):
    output = []
    for i in range (1, int(listLine[0]) + 1):
        
        currentState = list(listLine[i])
        #print(currentState)
        counter = 0
        while (counter < len(currentState) - 1):
            if (currentState[counter] == currentState[counter + 1]):
                currentState.pop (counter)
            else:
                counter = counter + 1
        if (len (currentState) > 0 and currentState[len (currentState) - 1] == '+'):
            currentState.pop ()

            
        
        output.append ("Case #" + str(i) + ": " + str(len (currentState)))
        printOutput (output)
                   
        
                                         
def printOutput (output):
    outputFile = open('output', 'w')
    for i in range (0, len (output) - 1):
        outputFile.write (output[i] + "\n")
    outputFile.write (output[len (output) - 1])
            


readInput()
