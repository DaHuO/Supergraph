from math import sqrt
from itertools import count, islice

def isPrime(n):
    loops = 0
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if loops > 10000:
            break
        if not n%number:
            return [False,number]
        loops+=1
    return [True, 0]

def tobase10(n, base):
    nstr = str(n)
    digits = []
    for d in nstr:
        digits.append(int(d))
    sum = 0
    for i in range(len(digits)):
        exp = (len(digits)-i-1)
        sum+=digits[i]*(base**(exp))
    return sum

def generateJamcoins(n,j):
    inside = n-2
    jamcoins =[]
    factorlist = []
    for i in xrange(2**inside):
        binary = str(bin(i)).split('b')[1]
        while len(binary)!=n-2:
            binary = '0'+binary
        binary = '1'+binary+'1'
        coin = int(binary)
        base10 = []
        for base in range(2,11):
            base10.append(tobase10(coin,base))
        iscoin = True
        factors = []
        for number in base10:
            #print 'checking: '+str(number)
            result = isPrime(number)
            #print 'done'
            if result[0]:
                iscoin = False
                break
            else:
                factors.append(result[1])
        if iscoin:
            print coin
            jamcoins.append(coin)
            factorlist.append(factors)
        if len(jamcoins)==j:
            break
    return [jamcoins,factorlist]

f = open('C-large.in','r')
out = open('outL.txt','w')
case = 0
for line in f:
    if case == 0:
        case += 1
    else:
        print line
        nj = line.split(' ')
        results = generateJamcoins(int(nj[0]),int(nj[1]))
        out.write("Case #"+str(case)+": \n")
        for i in range(len(results[0])):
            factors = []
            for f in results[1][i]:
                factors.append(str(f))
            out.write(str(results[0][i])+' '+' '.join(factors)+'\n')
        case+=1
