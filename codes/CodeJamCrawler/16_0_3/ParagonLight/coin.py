import utils


def generateCoinJam(N):
    n = ['0'] * N
    n[0] = '1'
    n[N-1] = '1'
    return n

def updateCoin(coin):
    length = len(coin)
    for i in range(length-1):
        v = coin[length - i - 2]
        if v == '0':
            coin[length-i-2] = '1'
            return coin
        else:
            coin[length-i-2] = '0'
    return coin

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return -1, True
    if n == 3:
        return -1, True
    if n % 2 == 0:
        return 2, False
    if n % 3 == 0:
        return 3, False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i, False

        i += w
        w = 6 - w

    return -1, True

def getBase(coin, N, b):
    n = 0
    for i in range(len(coin)):
        n += b**(N-1-i) * int(coin[i]) 
    return n

def findDivisor(coin, i, N):
    n = getBase(coin, N, i)
    return isprime(n)

if __name__ == "__main__":
    inputFile = "inputQ3"
    inputFile = "C-small-attempt0.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ3"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        outputString = "Case #" + str(index)+ ":\n"
        print outputString
        outputData.write(outputString)
        rowData = inputData.next()
        rowData = rowData.strip()
        strs = rowData.split(' ')
        N = int(strs[0])
        J = int(strs[1])
        term = True
        n = 0
        coin = generateCoinJam(N)
        while term:
            coinString = ''.join(coin)
            outputString = ""
            outputString += coinString
            result = False
            for i in range(2,11):
                divisor, result = findDivisor(coin, i, N)
                if not result:
                    outputString += " "
                    outputString += str(divisor)
                else:
                    break
            if not result:
                outputString += "\n"
                print outputString
                outputData.write(outputString)
                n += 1
                if n == 50:
                    term = False
            coin = updateCoin(coin) 
            if coin[0] == '0':
                print 'error'






            
