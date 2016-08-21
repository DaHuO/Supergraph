import os, math



def bin2base(num, base):
    multiplier = 1
    newNum = 0
    while len(num) != 0:
        if num[-1] == "1":
            newNum += multiplier
        multiplier *= base
        num = num[:len(num)-1]
    return newNum

def isPrime(n):
    if n == 0 or n == 1: return 0
    if n == 2: return 0
    if n%2 == 0: return 2
    for i in xrange(3,int(math.sqrt(n)),2):
        if n%i == 0:
            return i
    return 0

def isJam(bits):
    tempStr = bits
    if not(bits[0] == bits[-1] and bits[0] == "1"):
        return ""
    for b in xrange(2, 11):
        x = bin2base(bits, b)
        div = isPrime(x)
        if div == 0: return ""
        tempStr += " %d" %(div)
    return tempStr + "\n"

def generateBitsOfLen(x):
    val = int(math.pow(2.0,float(x)))-1
    L = []
    n = str(bin(val))[2:]
    #print n
    #print ("x:",x)
    #print("len:,",len(str(n)))
    #print(len(str(n)) == x)
    while len(str(n)) == x:
        #print "happens"
        L.append(n)
        val -= 1
        n = str(bin(val))[2:]
    return L


def solveJam(path):
    #with open(path, "rt") as fin:
    #    stuff = fin.read().splitlines()
    stuff = path.splitlines()

    
    string = ""
    for i in xrange(1, len(stuff)):
        string += "Case #%d:\n" %(i)
        vals = stuff[i].split()
        N = int(vals[0])
        J = int(vals[1])
        jamsFound = 0
        possibleJams = generateBitsOfLen(N)
        #print possibleJams
        for bits in possibleJams:
            #print bits
            temp = isJam(bits)
            if temp != "":
                jamsFound+=1
                string += temp +"\n"
            if jamsFound >= J:
                return string
            

def formatSolution(path):
    with open("solutionC small.txt", "wt") as fout:
        fout.write(solveJam(path))

