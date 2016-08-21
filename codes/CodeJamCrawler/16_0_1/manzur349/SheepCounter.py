import sys

class SheepCounter(object):
    DIGIT_ARRAY = ["0","1","2","3","4","5","6","7","8","9"]
    DIGITS = "0123456789"

    def restoreDIGIT_ARRAY(self):
        return ["0","1","2","3","4","5","6","7","8","9"]
    
    def allDigitsEncountered(self):
        outVal = True
        for digit in self.DIGIT_ARRAY:
            if digit in self.DIGITS:
                outVal = False
                break
        return outVal

    def determineEncounteredNumbers (self, theNum):
        for digit in theNum:
            if digit in self.DIGIT_ARRAY:
                self.DIGIT_ARRAY[int(digit)] = "X"

    def doATest(self, iterations):
        for i in range(1, iterations, 1):
            multiple = 1
            while not self.allDigitsEncountered():
                self.determineEncounteredNumbers(str(i * multiple))
                multiple += 1
                #if multiple > 10:
                #    break
            print str(i)
            print "Our Array"
            print self.DIGIT_ARRAY
            print str((multiple-1) * i)
            self.DIGIT_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getLastNumberBeforeSleep(self, startingNumber, caseNumber):
        outVal = ""
        if startingNumber == 0:
            outVal = "Case #" + caseNumber + ": INSOMNIA"
        else:
            multiple = 1
            while not self.allDigitsEncountered():
                self.determineEncounteredNumbers(str(startingNumber * multiple))
                multiple += 1
            outVal = "Case #" + caseNumber + ": " + str((multiple-1) * startingNumber)
            self.DIGIT_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        return outVal

def main():
    myFizzle = open(sys.argv[1], "r")
    loadedFile = []
    numberOfTestCases = int(myFizzle.readline())
    myLine = myFizzle.readline()
    while myLine:
        loadedFile.append(int(myLine))
        myLine = myFizzle.readline()
    myFizzle.close()
    myFizzle = open("results.txt", "w")
    sc = SheepCounter()
    for i in range(0, numberOfTestCases, 1):
        myFizzle.write(sc.getLastNumberBeforeSleep(loadedFile[i], str(i + 1)) + "\n")
    myFizzle.close()

main()
    
