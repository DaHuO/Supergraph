from math import sqrt, pow
import random

def appendEs2Sequences(sequences,es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):
    """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
    return reduce(appendEs2Sequences,lists,[])

def primefactors(n):
    '''lists prime factors, from greatest to smallest'''
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = primefactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]      # n is prime


##############################################################
### factorization of a natural ##################################
##############################################################

def factorGenerator(n):
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def findDivisors(n):
    factors = factorGenerator(n)
    listexponents=[map(lambda x:k**x,range(0,factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        num = reduce(lambda x, y: x*y, f, 1)
        if num == 1 or num == n:
            continue
        else:
            return num
            break
    return None

def generateJamCoinOfLength(size):
    coin = "1"
    for i in range(0, size - 2):
        coin += str(random.randint(0, 1))
    coin += "1"
    return coin

def convertToBaseX(jamcoin, x):
    jamcoin = str(jamcoin)[::-1]
    number = 0
    for i in range(len(jamcoin) - 1, -1, -1):
        if int(jamcoin[i]) == 1:
            number += int(jamcoin[i]) * pow(x, i)
    return int(number)

inputFile = open("C-small-attempt0.in", "r")
outputFile = open("output.out", "w")

t = int(inputFile.next())
nAndj = inputFile.next()
n = int(nAndj[0:2])
print "n: " + str(n)
j = int(nAndj[3:5])
print "j: " + str(j)

for i in range(1, t + 1):
    print "Case #" + str(i) + ":"
    outputFile.write("Case #" + str(i) + ":" + "\n")
    legitJamCoins = []
    while len(legitJamCoins) != j:
       jamCoin = generateJamCoinOfLength(n)
       print "Trying: " + jamCoin
       baseNumbers = []
       divisors = []
       for k in range(2, 11):
           baseNumber = convertToBaseX(jamCoin, k)
           baseNumbers.append(baseNumber)
           # print "Find divisor for: " + str(baseNumber) + " (base" + str(k) + ")"
           divisor = findDivisors(baseNumber)
           if divisor is None:
               break
           else:
               # print "divisor found: " + str(divisor)
               divisors.append(divisor)
       if len(divisors) == 9:
           legitJamCoins.append(jamCoin)
           resultString = jamCoin + " "
           for d in divisors:
               resultString += str(d) + " "
           print resultString
           outputFile.write(resultString + "\n")
           # print baseNumber
           # print divisors




