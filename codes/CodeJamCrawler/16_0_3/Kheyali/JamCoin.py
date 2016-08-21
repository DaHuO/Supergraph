def smallestDivisor(num):
    numToStart = int(num ** 0.5)
    if num > 1:
        noOfLoop = 0
        for i in range(2,numToStart):
            if (num % i) == 0:
                return i
            if noOfLoop > 10000:
                return -1
            noOfLoop = noOfLoop +1
        return -1
    else:
        return -1


def convertToDecimal(binaryStr, baseNo):
    decimalNo = 0
    lengthOfStr = len(binaryStr)
    for i in range(0,lengthOfStr):
        decimalNo = decimalNo + int(binaryStr[i])*(baseNo**(lengthOfStr-i-1))
    return decimalNo

def changeBaseFromTen(num, base):
    alldigits = "0123456789"
    if num < 0 or base < 2 or base > 36:
        return ""
    generatedStr = ""
    while 1:
        generatedStr = alldigits[int(num % base)] + generatedStr
        num = int(num / base)
        if num == 0:
            break
    return generatedStr

def getSmallestNoForJamCoin(lenofcoin, base):
    return (base**(lenofcoin-1))+1

def getLargestNoForJamCoin(lenofcoin, baseNo):
    decimalNo = 0
    for i in range(0,lenofcoin):
        decimalNo = decimalNo + 1*(baseNo**(lenofcoin-i-1))
    return decimalNo

def findnJamCoinAndPrint(length, noOfCoins):
    smallestJamCoin = getSmallestNoForJamCoin(length,2)
    largestJamCoin = getLargestNoForJamCoin(length,2)

    for num in range(smallestJamCoin,largestJamCoin+1):
        if(num % 2) == 0:
            continue
        binaryStr = changeBaseFromTen(num,2)
        numList =[]
        baseCovered = 0
        for i in range(2,11):
            #print("Starting to check :"+str(convertToDecimal(binaryStr,i)))
            divisor = smallestDivisor(convertToDecimal(binaryStr,i))
            if divisor == -1:
                numList =[]
                baseCovered = 0
                break
            else:
                #print("Starting to check :"+str(convertToDecimal(binaryStr,i)),end=" ")
                numList.append(divisor)
                baseCovered += 1

        if baseCovered == 9 and noOfCoins > 0:
            print(binaryStr,end=" ")
            for j in range(len(numList)-1):
                print(numList[j],end=" ")
            print(numList[len(numList)-1])
            noOfCoins = noOfCoins -1
        if noOfCoins == 0:
            return

noofTestCases = int(input().strip())
for i in range(noofTestCases):
    length,noofcoin = input().split(" ")
    length,noofcoin = int(length),int(noofcoin)
    print("Case #"+str(i+1)+":")
    findnJamCoinAndPrint(length,noofcoin)
