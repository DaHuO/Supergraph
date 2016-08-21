#Gettubg the Digits
import sys

def readInput (filename):
    cases = []
    with open (filename, 'r') as file:
        numberOfCases = int(file.readline())
        for i in range(numberOfCases):
            cases.append(file.readline().replace('\n',''))
    return numberOfCases, cases

def writeOutput (filename, output, numberOfCases):
    with open (filename, 'w') as file:
        for i in range(numberOfCases):
            line = "Case #" + str(i+1) + ": "
            line +=  output[i]
            line += '\n'
            file.write(line)

def problem (inputfile=".input", outputfile="output"):
    numberOfCases, cases = readInput(inputfile)
    output = []
    for case in cases:
        output.append(SearchDigit(case))
    writeOutput(outputfile, output, numberOfCases)

stringNumbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def SearchDigit (stringS):
    unorderedString = createDict(stringS) 
    cont = 0
    ans = DFS (cont, unorderedString)
    ans = [str(i) for i in ans]
    return "".join(ans)

def createDict (unorderedString):
    stringDict = dict()
    for character in unorderedString:
        if character in stringDict:
            stringDict[character] += 1
        else:
            stringDict[character] = 1
    return stringDict

def DFS (cont, unorderedString):
    if cont > 9:
        return None
    word = stringNumbers[cont]
    newString = isWordInString(word, unorderedString)
    if newString == {}:
        return [cont]
    if newString:
        ans = DFS(cont, newString)
        if ans != None:
            return [cont] + ans
    return DFS(cont+1, unorderedString)

def isWordInString (word, iunorderedString):
    unorderedString = iunorderedString.copy() 
    for character in word:
        if (character in unorderedString):
            unorderedString[character] -= 1
            if unorderedString[character] == 0:
                del unorderedString[character]
        else:
            return None
    return unorderedString

if __name__ == "__main__":
    problem(sys.argv[1])
