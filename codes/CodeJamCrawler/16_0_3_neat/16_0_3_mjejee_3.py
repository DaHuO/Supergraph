size = int (raw_input())

i=0

def get_primes (max):
    def check_prime (n, primelist):
        for prime in primelist:
            if n % prime == 0:
                return False
        return True
    l = []
    n= 1
    while n < max:
        n +=1
        if check_prime(n, l):
            l.append(n)
    return l

def getnumbernontrivial (n):
    if n in primes:
        return None
    p = [x for x in primes if x<=n ]
    for i in p:
        if n % i == 0:
            return i
        i+=1
    return None #No primes found

def getjamcoinnontrivial (jamcoin):
    l = [jamcoin]
    for i in range (2,11):
        nontrivial = getnumbernontrivial(int(jamcoin,i))
        if nontrivial is None:
            return None
        l.append(str(nontrivial))
    return ' '.join(l)

def processjamcoin(n, j):
    lines = []
    jamcoin_int = 0
    for i in range (j):
        while True:
            varpart = "{0:b}".format(jamcoin_int).zfill(n-2)
            jamcoin = '1'+varpart+'1'
            nontrivial = getjamcoinnontrivial(jamcoin)
            jamcoin_int += 1
            if nontrivial is not None: #Non trivial values found for this jamcoin
                lines.append(nontrivial)
                break
    return lines


#Only use the first primes until 100000 for checking if a number is evenly divisible
#It can produce false negatives, but it avoids excesive resource comsuption.
primes = get_primes(100000)

while True:
    if i>=size:
        break
    i = i+1
    linearray = raw_input().split(' ')
    print 'Case #'+ str(i) + ':'
    for line in processjamcoin(int(linearray[0]),int(linearray[1])):
        print line
