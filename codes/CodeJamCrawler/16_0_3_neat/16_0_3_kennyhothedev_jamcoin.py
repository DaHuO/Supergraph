import itertools
import math

def jamCoin(n, k):

    BStrings = {}
    counter = 0

    for middleBString in itertools.product("01", repeat = n-2):

        if counter == k:
            break

        totalBString = "1" + ''.join(middleBString) + "1"
        baseList = getBaseList(totalBString)


        if baseList[0]:
            BStrings[totalBString] = baseList[1]

            for n in range(len(BStrings[totalBString])):
                BStrings[totalBString][n] = getDivisor(BStrings[totalBString][n])
            counter += 1
    return BStrings


def getBaseList(bString):
    baseList = [[True],[]]
    for i in range(2,11):
        baseNum = int(bString,i)
        if isPrime(baseNum):
            baseList[0] = False
            break
        else:
            baseList[1].append(baseNum)
    return baseList

def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

def getDivisor(n):
    counter = 2
    while n % counter != 0:
        counter += 1
    return counter

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  bStringLength, numberOfBstrings = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

  validBStrings = jamCoin(bStringLength, numberOfBstrings)
  print "Case #{}:".format(i)

  for key in validBStrings:

  		
  		print "{}".format(key + " " + (" ".join(str(n) for n in validBStrings[key])))
  	




  # check out .format's specification for more formatting options