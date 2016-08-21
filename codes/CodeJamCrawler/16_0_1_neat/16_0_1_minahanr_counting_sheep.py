inputFile = open("inputFile.txt", 'r')
outputFile = open("outputFile", 'w')
def countSheep(prevNumber, number, digitsLeft):
    """
    prevNumber, number = Int
    digitsLeft = dict of digits 0-9, corresponding to True if the digit hasn't been seen, False otherwise
    
    """
    strNum = sorted(set(str(number)))
    if number == 0:
        return "INSOMNIA"
    #updates digits she has seen based on the number    
    for digit in strNum:
        if digitsLeft[digit] == True:
            digitsLeft[digit] = False
    #Checks to see if all values in digitsLeft have been seen. If so, it returns the number.
    if sum(digitsLeft.values()) == 0:
        return str(number)
    return countSheep(number, number + number - prevNumber, digitsLeft)

def runTrials(numTrials, initialNumbers):
    results = ""
    for trial in range(numTrials):
        results += "Case #{}: {}\n".format(str(trial+1), countSheep(0, initialNumbers[trial], \
            {"0": True, "1": True, "2": True, "3": True, "4": True, "5": True, \
            "6": True, "7": True, "8": True, "9": True}))
    return results
            
trialData = inputFile.readlines()
print runTrials(int(trialData[0]), [int(trialData[x]) for x in range(1, len(trialData))])
outputFile.write(runTrials(int(trialData[0]), [int(trialData[x]) for x in range(1, len(trialData))]))
