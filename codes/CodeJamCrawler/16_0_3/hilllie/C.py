import math
import itertools

filename = "C"


def readFile():
    with open(filename+".in") as f:
        lines = [line.strip().split() for line in f.readlines()[1:]]
        return lines


#def convertToBase(input, base):

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return 2
    if n < 9: return True
    if n%3 == 0: return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print '\t',f
        if n%f == 0: return f
        if n%(f+2) == 0: return f+2
        f += 6
        if f > 10000:
            return True
    return True    


def isJamcoin(jamString):
    res = []
    for base in range(2, 11):
        primeBase = is_prime(int(jamString, base))
        if primeBase is True:
            return False
        else:
            res.append(primeBase)
    return res

def sanityCheck(jamCoin, factors):
    for base in range(2, 11):
        if not int(jamCoin, base) % int(factors[base-2]) == 0:
            print "error"
            exit()
    
def writeRes(results):
    resText = "Case #1:\n"
    print "results:"
    for res in results:
        jamCoin = str(res[0])
        factors = [str(item) for item in res[1]]
        sanityCheck(jamCoin, factors)
        resText += jamCoin + " " + " ".join(factors) + "\n"
    print resText
    with open(filename+".out", "w") as f:
        f.write(resText)
    


def main(lines):
    print lines
    #print isJamcoin("11")
    #exit()
    ctr = 0
    results = []
    for line in lines:
        N, J = line
        N, J = int(N), int(J)
        for item in itertools.product('01', repeat=N-2):
            curr = "1"+"".join(item)+"1"
            res = isJamcoin(curr)
            if isJamcoin(curr):
                ctr+=1
                print ctr, curr, res
                results.append([curr, res])
                if ctr==J:
                    break
    writeRes(results)
            #print curr

lines = readFile()
main(lines)
