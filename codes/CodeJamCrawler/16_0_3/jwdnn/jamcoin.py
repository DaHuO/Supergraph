#coinjam

def getvalue(jamcoin):
    values = []
    for i in range(2,11):
        values.append(int(jamcoin,i))
    return values

def isPrime(num):
    if num ==2:
        return True
    elif num%2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True

def isJamcoin(s):
    if s[0] != '1' or s[-1] != '1':
        return False
    vals = getvalue(s)
    for v in vals:
        if isPrime(v):
            return False
    return True

def base2(num):
    newNum = ''
    while num != 0:
        remainder = num%2
        num = num //2
        newNum += str(remainder)
    return newNum

def getfactor(num):
    for i in range(2,num//2):
        if num%i == 0:
            return i

def factorString(l):
    newStr = ''
    for f in l:
        newStr+=(' '+str(f))
    return newStr

#open files
inputFile = open('testJamcoin.in','r')
out = open('jamcoinOut.out','w')

T = int(inputFile.readline().strip())
N,J = inputFile.readline().strip().split()
N = int(N)
J = int(J)
start = 2**(N-1)+1
coins = []
coin = '0'*N

for t in range(T):
    out.write("Case #%d:\n"%(t+1))
    while len(coins) < J and len(coin)==N:
        coin = bin(start)[2:]
        if isJamcoin(coin):
            coins.append(coin)
        start += 2
    
    factors = []
    for c in range(J):
        factors.append([])
        for v in getvalue(coins[c]):
            factors[c].append(getfactor(v))
        out.write(coins[c]+factorString(factors[c])+'\n')

inputFile.close()
out.close()