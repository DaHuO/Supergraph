import sys

def flipPancakes ( pancakeString ) :
    outputString = ""

    if pancakeString[0] == "+":
        for i in pancakeString:
            outputString += "-"
    else:
        for i in pancakeString:
            outputString +="+"

    return outputString



def pancakes( stackOfPancakes ):

    pancakeStack = ""
    counter = 0

    for i in stackOfPancakes:
        if len(pancakeStack) == 0:
            pancakeStack += i
            continue
        elif (len(pancakeStack) > 0 and i == pancakeStack[-1]):
            pancakeStack += i
            continue
        else:
            pancakeStack = flipPancakes(pancakeStack)
            pancakeStack += i
            counter += 1
            continue

    if pancakeStack[0] == "+":
        return counter
    else:
        return counter + 1

numTests = input()

for i in range (0, int(numTests)):
    print ("Case #" + str(i+1) +": " + str(pancakes(input())))
