#Test a string like '100101' to see if it's a jamcoin
#Return false if it's not a jamcoin
#Return the list of divisors if it is (ex: [3, 5])
def testCoin(jamcoin):
    #print(jamcoin)
    divisors = [jamcoin]
    for i in range(2, 11): #base 2 through base 10
        actualNumber = int(jamcoin, i)
        divisor = 2
        while (divisor <= actualNumber / 2 and divisor < 30):
            #print("divisor is " + str(divisor) + " and actualNumber is " +str(actualNumber))
            if (actualNumber % divisor == 0):
                divisors.append(divisor)
                break
            else:
                divisor += 1
    #print(divisors)
    if (len(divisors) < 10):
        return False
    else:
        return divisors


def generateCoins():
    jamcoins = []
    currentNumber = 0
    
    #maxNumber = coinLength * coinLength - 1 #ex: 15 (inclusive)

    while (len(jamcoins) < numberOfJamcoinsToGenerate):
        currentCoin = ('{:0' + str(lengthOfJamcoin - 2) + 'b}').format(currentNumber) #ex: '0000'
        currentCoin = "1" + currentCoin + "1" #ex: 100001
        result = testCoin(currentCoin)
        if (result != False): #We found a valid jamcoin!
            #print("found a jamcoin!")
            jamcoins.append(result)
        currentNumber += 1
    return jamcoins
    

lineNum = 0
finishedCases = []

with open('C-large.in') as f:
    for line in f:
        line = line.rstrip()
        lineNum += 1
        if (lineNum == 1): #The first line is the #of cases
            numCases = int(line)
        elif (lineNum == 2):
            splitLine = line.split(" ")
            #print(splitLine)
            lengthOfJamcoin = int(splitLine[0])
            #print("each jamcoin will have a length of " +str(lengthOfJamcoin))
            numberOfJamcoinsToGenerate = int(splitLine[1])
            #print("there will be " + str(numberOfJamcoinsToGenerate) + " jamcoins")


jamcoins = generateCoins()

#print(testCoin('100011'))
#print(testCoin('111111'))
#print(testCoin('111001'))
#print(testCoin('110111'))
#print(testCoin('110011'))


outputFile = open('coinjam.out', 'w')
outputFile.write('Case #1:\n')
for i in range(len(jamcoins)):
    for j in range(len(jamcoins[i])):
        if (j != 0):
            outputFile.write(' ') #spacing
        outputFile.write(str(jamcoins[i][j]))
    if (i != len(jamcoins) - 1):
        outputFile.write('\n') #spacing
outputFile.close()
print("done!")
