import time
outputFile = open('outputFile', 'w')
def addToList(array, item):
    array.append(item)
    return array

def produceAllBinariesOfLength(length):
    if length == 1:
        return [[0], [1]]
    return [addToList(x, 0) for x in produceAllBinariesOfLength(length-1)] + [addToList(x, 1) for x in produceAllBinariesOfLength(length-1)]

def binaryIterator(length):
    binaryNum = ["0"] * length
    yield binaryNum
    while sum([int(x) for x in binaryNum]) < length:
        location = None
        for iterator in xrange(length-1, -1, -1):
            if binaryNum[iterator] == "0":
                binaryNum[iterator] = "1"
                location = iterator
                break
        for i in xrange(location+1, len(binaryNum)):
            binaryNum[i] = "0"
        yield binaryNum

def isNotPrime(n):
    if n == 2:
        return False
    if n == 3:
        return False
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return False
    
def isJamcoin(number):
    if number[0] != "1" or number[-1] != "1":
        return False
    bases = []
    for base in xrange(2, 11):
        bases.append(sum([int(number[x]) * (base ** (len(number) - x - 1)) for x in xrange(len(number))]))
    #for n in range(len(bases)):
    #    print "Base {}: {} is {}\n".format(str(n + 2), str(bases[n]), isNotPrime(bases[n]))
    divisors = [str(isNotPrime(x)) for x in bases]
    if 'False' in divisors:
        return False
    else:
        return divisors
    
def findJamcoinsOfLength(length, numJamcoins):
    s = time.time()
    jamcoinsFound = 0
    results = ""
    for i in binaryIterator(length-2):
        i = ["1"] + i + ["1"]
        jamcoin = isJamcoin(i)
        if jamcoin != False:
            jamcoinsFound += 1
            if jamcoinsFound %5 == 0:
                print jamcoinsFound
            results += "{} {}\n".format("".join(i), " ".join(jamcoin))
            if jamcoinsFound >= numJamcoins:
                print time.time() - s
                outputFile.write(results)
                return results