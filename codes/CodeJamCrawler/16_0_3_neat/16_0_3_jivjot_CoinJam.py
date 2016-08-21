import random

def getPrimeNumbers(N):
    flag = [True] * (N + 1)
    flag[0] = flag[1] = False
    ret = set()
    for i in range(2,int(N**0.5) +1):
        if flag[i] == True:
            j = 2
            while i*j <= N:
                flag[i*j] = False
                j = j+1
    for i in range(0,len(flag)):
        if flag[i] == True:
            ret.add(i)
    return ret

primes = getPrimeNumbers(100)

def generateCand(N):
    s = ""
    for i in range(0,N-2):
        r = random.randint(0, 1)
        s = s + str(r)
    s = "1" + s + "1"
    return s

#print generateCand(32)
#print generateCand(32)

def convertBase(candidate,base):
    res = 0
    rev = candidate[::-1]
    for i in range(0,len(candidate)):
        if rev[i] == '1':
            res = res + base**i
    return res

def isPrime(no):
    for i in primes:
        if no % i == 0:
            return False,i
    return True,0

def checkCand(candidate):
    arr = []
    for base in range(2,11):
        no = convertBase(candidate,base)
        res = isPrime(no)
        if res[0] == True:
            return (False,res[1])
        arr.append(res[1])
    return (True,arr)



test = int(raw_input())
for i in range(0,test):
    res = {}
    N,J = map(int,raw_input().split())
    while len(res) != J:
        candidate = generateCand(N)
        if candidate not in res:
            isValid = checkCand(candidate)
            if isValid[0] == True:
                res[candidate] = isValid[1]
    print "Case #"+str(i+1)+":"
    for i in res:
        arr = [str(i)] + map(str,res[i])
        print ' '.join(arr)


