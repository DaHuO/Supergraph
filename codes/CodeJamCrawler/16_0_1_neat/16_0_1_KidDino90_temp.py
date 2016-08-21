

f = open ('A-large.in', 'r')


def main ():
    listLine = f.read ().splitlines ()        
    check (listLine)

def check (listLine):
    output = []
  
    for i in range (1, len(listLine)):
        tempList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
        if (int (listLine[i]) == 0):
            output.append ("Case #" + str (i) + ": INSOMNIA")
        else:
            
            originalNumber = listLine[i]            
            currentNumber = originalNumber
            
            for k in range (0, len (currentNumber)):
                if (currentNumber[k] in tempList):
                    tempList.remove (currentNumber[k])
            
                    
            while (len (tempList) != 0):
                currentNumber = str (int (currentNumber) + int (originalNumber))
                #print (currentNumber)   
                for k in range (0, len (currentNumber)):
                    if (currentNumber[k] in tempList):
                        tempList.remove (currentNumber[k])
            output.append ("Case #" + str (i) + ": " + currentNumber)
    printOutput(output)
                                     
def printOutput (output):
    outputFile = open('output', 'w')
    for i in range (0, len (output) - 1):
        outputFile.write (output[i] + "\n")
    outputFile.write (output[len (output) - 1])
            


main()
