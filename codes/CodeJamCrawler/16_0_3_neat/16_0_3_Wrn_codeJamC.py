import math
import random

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def getPrimeArray(n):
    pArray = range( 2, int(math.sqrt(n))+1)
    i = 0
    while i < len(pArray) :
        #print "loop i{}:".format(i) , pArray
        p = pArray[i]
        j = i+1
        while j < len(pArray) :
            #print "loop j{}:".format(i) , pArray
            if pArray[j] % p == 0 :
                #print "pop ",  pArray[j]
                pArray.pop(j)
            else:
                j = j+1
        i = i+1
    return pArray

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def getAllBase(coin):
    l = []
    for base in range(2,10+1) :
        n = 0
        for i in range(len(coin)):
            if coin[i] == '1':
                n += int(math.pow(base,len(coin)-i-1))
        l.append(n)
    return l

##def isJamCoin(coin):
##    r = 9*[0]
##    l = getAllBase(coin)
##    #print l
##    global pArray
##    #print pArray
##    for p in pArray:
##        #print r
##        for i in range(len(l)) :
##            if( r[i] == 0 ):
##                if( l[i] % p == 0 ):
##                    r[i] = p
##    #print r
##    if r.count(0) == 0 :
##        return r
##    return []

def isJamCoin(coin):
    r = 9*[0]
    l = getAllBase(coin)
    #print l
    #pArray = getPrimeArray(l[8])
    #print pArray
    #for p in pArray:
        #print r
    for i in range(len(l)) :
        for c in range(2,int(l[i]**0.5)+1):
            if l[i]%c==0:
                r[i] = c
                break
    #print r
    if r.count(0) == 0 :
        return r
    return []

def randomCoin( N ):
    coin = N*[0]
    coin[0] = 1
    coin[N-1] = 1
    n = random.randint(0, N-2)
    count = 0
    while count < n :
        pos = random.randint(1,N-1)
        if coin[pos] != 1 :
            count += 1
            coin[pos] = 1
    return coin

def getNextCoin( k, N ):
    return '1' + ("{0:0"+str(N-2)+"b}").format(k)+ '1'

def solve( J, N ):
    count = 0
    solList = []
    k = 0
    print "Case #1:"
    #maxCoin = int(N*'1')
    #global pArray
    #pArray = primes2(int(math.sqrt(maxCoin))+1)
    #print pArray
    while count < J :
        coin = getNextCoin( k, N )
        #print ">>>",coin
        k += 1
        r = isJamCoin( coin )
        
        if r != [] :
            if coin not in solList:
                solList.append( coin )
                print coin,
                for a in r :
                    print a,
                print ''
                count += 1
                
solve(50,16)
