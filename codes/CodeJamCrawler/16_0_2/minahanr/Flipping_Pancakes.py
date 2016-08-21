inputFile = open('inputFile.txt', 'r')
outputFile = open('outputFile', 'w')

class PancakeStack(object):
    def __init__(self, pancakes):
        self.pancakes = pancakes
    
    def isFlippedCorrectly(self):
        return sum(self.pancakes) == len(self.pancakes)
            
    def flip(self, location):
        for pancake in xrange(0, location+1):
            if self.pancakes[pancake] == True:
                self.pancakes[pancake] = False
            elif self.pancakes[pancake] == False:
                self.pancakes[pancake] = True
                
    def findFlipLocation(self):
        for pancake in range(len(self.pancakes) - 1, -1, -1):
            if self.pancakes[pancake] == False:
                return pancake
        
def makePancakes(pancakes):
    newPancakes = []
    for pancake in list(pancakes):
        if pancake == "+":
            newPancakes.append(True)
        elif pancake == "-":
            newPancakes.append(False)
    return PancakeStack(newPancakes)

def servePancakes(pancakes):
    pancakes = makePancakes(pancakes)
    numFlips = 0
    while not pancakes.isFlippedCorrectly():
        numFlips += 1
        pancakes.flip(pancakes.findFlipLocation())
    return numFlips
    
    
def pancakeTrial(numTrials, pancakeTrials):
    results = ""
    for trial in xrange(numTrials):
        results += "Case #{}: {}\n".format(trial + 1, servePancakes(pancakeTrials[trial]))
    return results
        
trialData = inputFile.readlines()
print pancakeTrial(int(trialData[0]), trialData[1:])
outputFile.write(pancakeTrial(int(trialData[0]), trialData[1:]))
    
