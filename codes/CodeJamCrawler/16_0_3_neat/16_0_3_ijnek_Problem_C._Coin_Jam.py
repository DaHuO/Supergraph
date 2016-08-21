def checkPrime(n): #returns True/False and factor
    """Returns True if n is prime."""
    if n == 2:
        return True,0
    if n == 3:
        return True,0
    if n % 2 == 0:
        return False,2
    if n % 3 == 0:
        return False,3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False,i

        i += w
        w = 6 - w
        if i > 30:
            return True,0

    return True,0

def convertToBase(arrayNumberBinary,base):
    numberInBase = 0
    lengthBinary = len(arrayNumberBinary)
    for i in range(lengthBinary):
        numberInBase += int(arrayNumberBinary[i])*(base**(lengthBinary-i-1))
    return numberInBase

def checkJamCoin(numberInDecimal):
    arrayNumberBinary = list(str(bin(numberInDecimal)))[2:]
    factorList = [] #stores all factors
    for base in range(2,11):
        numberInBase = convertToBase(arrayNumberBinary,base)
        isPrime, factor = checkPrime(numberInBase)
        if isPrime:
            return False,0
        else:
            factorList.append(factor)
    return True,factorList


file_object= open('input.txt','r')
file_object2 = open('output.txt','w')

t = int(file_object.readline().rstrip('\n'))

file_object2.write("Case #1:\n")
n,j = map(int,file_object.readline().split())
foundCount = 0 #increment when found
numberInDecimal = 2**(n-1) + 1
while foundCount < j:
    isJamCoin, factorArray = checkJamCoin(numberInDecimal)
    if isJamCoin:
        foundCount += 1
        file_object2.write(''.join(list(bin(numberInDecimal))[2:])+' '+' '.join([str(x) for x in factorArray])+'\n')
        print(foundCount)
        #convert numberInDecimal to binary
        #print numberInBinary, and sequence of factors
    numberInDecimal += 2 #as last digit must be 1, +=2 would increment the second last digit