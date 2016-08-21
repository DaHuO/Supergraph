import sys

def parseFileName(filename, mode="rt"):
    outputArray = []
    i = 0
    with open(filename, mode) as fin:
        for line in fin:
            if i != 0:
                printOutput(i, line)
            i += 1
    return outputArray

def getListOfDigits(n):
    n = int(n)
    digitsSet = set()
    while n > 0:
        onesDigit = n % 10
        digitsSet.add(onesDigit)
        n = n // 10
    return digitsSet

def round1(N):
    N = int(N)
    if N == 0: return "INSOMNIA"
    digitsSeen = set()
    i = 1
    while len(digitsSeen) != 10:
        digitsSeen = digitsSeen.union(getListOfDigits(N*i))
        i += 1
    return str(N*(i-1))

def printOutput(i, N):
    print ("Case #%d: " + round1(N)) % i

def main():
    parseFileName(sys.argv[1])

if (__name__ == "__main__"):
    main()




