def runCases(fname,outname):
    case = 0
    with open(fname,'rU') as f:
        for line in f:
            if case == 0: 
                cases = int(line)
                case+=1
                continue
            if case > cases: break
            coinJam(line,case,outname)
            case+=1
    
def getDecimal(strNum, base):
    num = 0
    for i in range(len(strNum)):
        num += int(strNum[i])*(base**(len(strNum)-i-1))
    return num
    
def findDivisor(dec,primes):
    for p in primes:
        if dec % p == 0: return p
    return -1

def nextCoin(strNum):
    num = long(strNum)
    i = 1
    if strNum[-2] == '0':
        return str(num+10)
    num += 9*(10**i)
    while '2' in str(num):
        i+=1
        num += 8*(10**i)
    return str(num)
            
def findCoinJams(length,numCoins,outname):
    strNum = str(10**(length-1)+1)
    primes = getPrimes(2**(length/2+1))
    found = 0
    while len(strNum) == length and found < numCoins:
        divisors = isCoinJam(strNum,primes)
        #print strNum,divisors
        if divisors is not None:
            outputCoin(strNum, divisors, outname)
            found += 1
            #print found
        strNum = nextCoin(strNum)
    
def isCoinJam(strNum,primes):
    divisors = []
    for base in range(2,11):
        dec = getDecimal(strNum,base)
        num = findDivisor(dec,primes)
        if num == -1: return None
        else: divisors.append(num)
    return divisors
                  
def coinJam(line,case,outname):
    out = open(outname,'w')
    out.write("Case #1:\n")
    out.close()
    splitline = line.split(" ")
    length = int(splitline[0])
    numCoins = int(splitline[1])
    findCoinJams(length,numCoins,outname)
    
def outputCoin(strNum,divisors,outname):
    out = open(outname,'a')
    out.write(strNum)
    for div in divisors:
        out.write(" "+str(div))
    out.write("\n")
    out.close()
    
def isPrime(num,primes):
    for p in primes:
        if num % p == 0: return False
    return True
    
def getPrimes(maxNum):
    primes = [2]
    x = 3
    while x < maxNum:
        if isPrime(x,primes):
            primes.append(x*1)
        x += 2
    return primes


runCases("C-large.in","C-large.out")   