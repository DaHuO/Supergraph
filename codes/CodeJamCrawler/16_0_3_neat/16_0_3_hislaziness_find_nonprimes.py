import cPickle
import math

def dumb_is_prime(n):
    if n % 2 == 0:
        return 2
    lim = int(math.sqrt(n))
    for d in xrange(3,lim+1,2):
        if n % d == 0:
            return d
    return 0

def create_coins(n):
    start = int('1' + '0' * (n-2) + '1',2)
    end = int('1' * n,2)
    while start <= end:
	yield start
	start += 2

for i in range(2,33):
    jamcoins = {}
    for c in create_coins(i):
        coin = str(bin(c)[2:])
        factors = []
        for b in range(2,11):
            f = dumb_is_prime(int(coin,b))
            if f == 0:
                break
            factors.append(f)
        if len(factors) == 9:
            jamcoins[coin] = factors[:]
            if len(jamcoins) >= 50:
                break
    fp = open("C:/VBD/ws/code/GCJ 2016/qual/P3/" + str(i) + ".jamcoins","wb")
    cPickle.dump(jamcoins,fp)
    fp.close()
    #print jamcoins
