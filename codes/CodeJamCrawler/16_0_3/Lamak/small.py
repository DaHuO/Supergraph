import random
import math

fw = open("output.out", "w")

def lrange(num1, num2, step = 1):

    while num1 < num2:
        yield num1
        num1 += step

def getCases():
    with open("C-large.in") as f:
        words = f.read().split() 
        yield {'t': 1, 'N': int(words[1]), 'J': int(words[2])}

def getMyCases():
    yield {'t': 1, 'N': 32, 'J': 500}

def genJamCoinCandidate(N):
    while True:
        n = random.getrandbits(N)
        n = n | (pow(2, N-1) + 1)
        yield n

def base(n, bits, base):
    m = 0
    for b in range(0, bits):
        p = pow(base, b)
        m = m + (p if pow(2, b) & n else 0)
    return m

def isPrime(n):
    if n % 2 == 0:
        return 2

    sqr = int(math.sqrt(n)) + 1
    for divisor in lrange(3, sqr, 2):
        if n % divisor == 0:
            return divisor
        elif divisor > 10000:
            return 0 #give up on this number
    return 0

def getBinary(b, l = -1):
    s = ''
    while b > 0:
        s = str(b % 2) + s
        b = b / 2
    if l > -1:
        while len(s) < l:
            s = '0' + s
    return s

divisorOrPrime = {}
processed = []
jamCoinsFound = 0
for T in getCases():
    fw.write('Case #1:\n')
    for n in genJamCoinCandidate(T['N']):
        if n not in processed:
            processed.append(n)
            bases = {}
            isJamCoin = True
            for b in range(2, 11):
                bases[b] = base(n, T['N'], b)
                dOrP = divisorOrPrime.get(bases[b], isPrime(bases[b]))
                divisorOrPrime[bases[b]] = dOrP
                if divisorOrPrime[bases[b]] == 0:
                    isJamCoin = False
                    break

            if isJamCoin:
                jamCoinsFound += 1
                print getBinary(n), divisorOrPrime[bases[2]], divisorOrPrime[bases[3]], divisorOrPrime[bases[4]], divisorOrPrime[bases[5]], divisorOrPrime[bases[6]], divisorOrPrime[bases[7]], divisorOrPrime[bases[8]], divisorOrPrime[bases[9]], divisorOrPrime[bases[10]]
                fw.write(getBinary(n))
                for b in range(2, 11):
                    fw.write(' ' + str(divisorOrPrime[bases[b]]))
                fw.write('\n')
            if jamCoinsFound == T['J']:
                break
            
    
    #fw.write('Case #' + str(T['t']) + ': ' + str(steps) + '\n')


fw.close()
