import numpy as np
outpFile = file('outputLargeC', 'w')
# outpFile = file('outputSmallC', 'w')
outpFile.write('Case #1:\n')
N = 32
J = 500

a1numOf0s = 1
a2numOf0s = 1
distance = 1
awhere0s = 0


def anotherGenerator():
    global a1numOf0s
    global a2numOf0s
    global distance
    global awhere0s
    if a1numOf0s + awhere0s + a2numOf0s + distance > N-2:
        a1numOf0s += 1
        awhere0s = 0
    jem =''
    for _ in xrange(awhere0s):
        jem += '1'
    for _ in xrange(a1numOf0s):
        jem += '0'
    for _ in xrange(distance):
        jem += '1'
    for _ in xrange(a2numOf0s):
        jem += '0'
    for _ in xrange(N-2-(a1numOf0s + awhere0s + a2numOf0s + distance)):
        jem += '1'
    awhere0s += 1
    return '1'+jem+'1'

numOf0s = 1
where0s = 0
def generateNew():
    global numOf0s
    global where0s
    if numOf0s > N-3:
        return anotherGenerator()
    if numOf0s + where0s > N-2:
        numOf0s += 1
        where0s = 0
    jem =''
    for _ in xrange(where0s):
        jem += '1'
    for _ in xrange(numOf0s):
        jem += '0'
    for _ in xrange(N-2-numOf0s-where0s):
        jem += '1'
    where0s += 1
    return '1'+jem+'1'

n = 10000000

sieve = np.ones(n/3 + (n % 6 == 2), dtype=np.bool)
sieve[0] = False
for i in xrange(int(n**0.5)/3+1):
    if sieve[i]:
        k = 3 * i + 1 | 1
        sieve[((k*k)/3)::2*k] = False
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
listOfPrimes = np.r_[2, 3, ((3*np.nonzero(sieve)[0]+1) | 1)].tolist()


def getJemiDiv():
    global divisors
    global jemicoin
    for base in range(2, 11, 1):
        jem = int(jemicoin, base)
        for prime in listOfPrimes:
            if prime > jem // 2:
                return False
            if jem % prime == 0:
                divisors.append(prime)
                break
    if len(divisors) == 9:
        return True
    else:
        return False

while J != 0:
    jemicoin = generateNew()
    divisors = []
    if getJemiDiv():
        outpFile.write(jemicoin)
        for divi in divisors:
            outpFile.write(' ' + str(divi))
        outpFile.write('\n')
        J -= 1

outpFile.close()
