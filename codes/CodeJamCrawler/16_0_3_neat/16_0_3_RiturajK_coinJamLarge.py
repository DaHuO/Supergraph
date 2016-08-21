import itertools as iter
import math
import operator

def findFactor(seed):
    factors = []
    for num in seed:
        j = 2
        while(j<=int(num**0.5)+1):
            if(num%j == 0):
                factors.append(j)
                break
            j = j+1
    return factors

def isPrime(seed):
    prime = 1
    for num in seed:
        j = 2
        while(j<=int(num**0.5)+1):
            if(num%j == 0):
                prime = 0
                break
            j = j+1
        if(prime == 1):
            return prime
    return prime

def isValidSeed(newSeed,seed):
    difference = map(operator.sub,newSeed,seed)
    for pos in range(9):
        a = seed[pos]
        b = difference[pos]
        #print a,' ',b
        while(a%b !=0):
            rem = a%b
            #print 'rem = ',rem
            a = b
            #print 'a = ',a
            b = rem
            #print 'b = ',b
            if(b==1):
                return 0
    return 1

def createSeed(val):
    global N
    decSeed = val
    binSeed = format(decSeed,'b')
    binSeed = map(int,list(binSeed))
    length = len(binSeed)
    pad = [0]*(N-2-length)
    binSeed = [1]+pad+list(binSeed)+[1]

    seed = []
    for base in range(2,11):
        multiplier = 1
        positions = range(N)
        positions.reverse()
        num=0
        for pos in positions:
            num = num + binSeed[pos]*multiplier
            multiplier = base*multiplier
        seed.append(num)
    return seed

f = open('E:\\Code Jam 2016\\JamCoin\\C-large.txt', mode = 'r')
fo = open('E:\\Code Jam 2016\\JamCoin\\out.txt', mode = 'w')

testCases = int(f.readline())

for case in range(1,testCases+1):
    output = 'Case #'+str(case)+':\n'
    fo.writelines(output)
    line = f.readline().split(' ')
    if(line[len(line)-1]=='\n'):
        line.remove('\n')
    line = map(int,line)
    N = line[0]
    J = line[1]

    decSeed = 0
    seed = createSeed(decSeed)
    prime = 1
    while(prime==1):
        prime = isPrime(seed)
        if(prime == 1):
            decSeed = decSeed+1
            seed = createSeed(decSeed)
    factors = findFactor(seed)
    #print seed
    #print factors
    output = str(seed[8])+' '+' '.join(str(e) for e in factors)+'\n'
    fo.writelines(output)
    #print output
    J = J - 1
    while(J!=0):
        decSeed = decSeed+1
        newSeed = createSeed(decSeed)
        valid = isValidSeed(newSeed,seed)
        if(valid == 1):
            factors = findFactor(newSeed)
            seed = newSeed
            #print seed
            #print factors
            output = str(seed[8])+' '+' '.join(str(e) for e in factors)+'\n'
            #print output
            fo.writelines(output)
            J = J -1
