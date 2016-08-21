from sys import argv
import itertools, random, math

# Read args
script, filename, outPath = argv
# vars
outFile = open(outPath,'w')

# generate binary numbers of length n
def binary (n):
    binaries = ["".join(seq) for seq in itertools.product("01", repeat=n-2)]
    for i in range(0,len(binaries)):
        binaries[i] = '1'+binaries[i]+'1'
    return binaries

# convert binary number to base
def convertFromBinary (num, base):
    res = 0;
    for i in range(0,len(num)):
        pos = len(num) - i - 1
        res = res + int(num[i])*(base**(pos))
    return res

# check if a number is prime
def isPrime(num):
    n = int(num, 2)
    return 2 in [n,2**n%n]

# check if a number is not prime
def isNotPrime(n):
    return (not isPrime(n))

# get divisors for n
def divisors(n):    
    return sorted(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# apply filter to list
def filterList (list, filter):
    return [elem for elem in list if filter(elem)]

def getNonTrivialDivisorInBase (num, base):
    res = -1
    numInBase = convertFromBinary(num, base)
    divsOfNumInBase = divisors(numInBase)
    if len(divsOfNumInBase) > 2:
        res = random.sample(divsOfNumInBase[1:len(divsOfNumInBase)-1],1)[0]
    return res

def generateJamCoin (binary):
    outputString = binary
    for k in range(2, 11):
        divisor = getNonTrivialDivisorInBase(binary, k)
        if (divisor == -1):
            return -1
        outputString += ' %d' % divisor
    outputString += '\n'
    return outputString

# Read file line by line into array
with open(filename) as f:
    content = f.readlines()
    numCases = int(content[0])
    for i in range(1, numCases+1):
        caseInput = content[i].split()
        numBits = int(caseInput[0])
        numAnswers = int(caseInput[1])
        binaries = filterList(binary(numBits), isNotPrime)
        answers = 0
        j = 0

        outFile.write('Case #%d:\n' %(i))

        while answers < numAnswers:
            outputString = generateJamCoin(binaries[j])
            if (outputString != -1):
                outFile.write(outputString)
                answers = answers + 1
            j = j + 1


outFile.close()
f.close()