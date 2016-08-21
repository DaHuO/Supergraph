import random
from math import sqrt
from itertools import count, islice

#reading input
f = open('C-small-attempt0.in','r')
out = open ('out','w')


#Helpers
def writeOut(case,value):
    output = "Case #" + str(case+1) + ": " + str(value)
    print output
    out.write(output + '\n')

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

def multiBases(case):
    case = case[::-1]
    basesValue = []
    for i in range(2,10+1):
        sum = 0
        for j in range(0,len(case)):
            sum += int(case[j])*pow(i,j)
        basesValue.append(sum)

    return basesValue


def checkJamCoin(case):
    if(case[0] == 0 or case[len(case)-1] == 0 ):
        return False

    #Check primality of all the bases
    for num in multiBases(case):
        if(isPrime(num)):
            return False

    return True


def getRandomNumber(N):
    ret = ''
    for i in range(0,N):
        if(i == 0 or i == N-1):
            ret += '1'
        else:
            ret += str(random.randint(0, 1))

    return ret

def getDivisors(case):
    divisorList = []
    for base in multiBases(case):
        isDivisor = False
        i = 2
        while(not isDivisor):
            if base % i == 0:
                isDivisor = True
                divisorList.append(i)
            i += 1

    return divisorList


#Read number of cases
numCases = int(f.readline())

#TESTING
case = ("100011")
a = multiBases(case)
outCase = case
for val in getDivisors(case):
    outCase = outCase + " " + str(val)
print outCase


for i in range(0,numCases):
    case = f.readline().strip('\n')
    J = int(case.split(" ")[0])
    N = int(case.split(" ")[1])
    numCount = 0
    writeOut(i,'')
    while(numCount < N):
        case = getRandomNumber(J)
        if(checkJamCoin(case)):
            numCount +=1
            outCase = case
            for val in getDivisors(case):
                outCase = outCase + " " + str(val)
            out.write(outCase +'\n')

