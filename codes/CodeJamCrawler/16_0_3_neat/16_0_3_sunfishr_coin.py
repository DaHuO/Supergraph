"""
Coin Jam

Produce J different jamcoins of length N

T is number of test cases
N is length of jamcoin string
J is number of different jamcoin strings

Small dataset
N = 16
J = 50

Large dataset
N = 32
J = 500

"""
import math
import itertools

input_file_name = 'C-small-attempt0.in'
output_file_name = 'C_small_coin.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

def nontrivialDivisorFor(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor

def primeFactorization(n):
    if n == 1:
        return [] # empty list
    else:
        p = nontrivialDivisorFor(n)
        return [p] + primeFactorization(n/p)

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True

def check(coin):    
    coinStr = ''.join(str(d) for d in coin) 
    # print coin 
    # print 'testing ', coinStr
    ntds = []
    isValid = True
    N = len(coin)
    for base in range(2,11):        
        value = 0

        for exp in range(N):
            index = N - exp - 1
            # print 'exp = %d' %exp, 'coin[exp] = %d' % coin[index]
            if coin[index] == 1:
                r = math.pow(base,exp)
                # print 'base = %d' % base, 'exp = %d' % exp, 'result = %d' %r
                value += r
        
        # print 'base = %d' % base, 'value = %d' % value
        if (isPrime(value)):
            # print 'fail!  Got a prime number: %d' % value, 'base = %d' % base
            isValid = False
            return False
        
        ntd = nontrivialDivisorFor(value)
        # divisor = int(value / ntd)
        # print ntd
        ntds.append(ntd)
        # print primeFactorization(value)

    if isValid:
        coinStr = ''.join(str(d) for d in coin)        
        ntdsStr = ''.join(str(n) + ' ' for n in ntds)
        # strip off any trailing space character
        ntdsStr = ntdsStr.strip()
        print coinStr, ntdsStr
        outFile.write(coinStr + ' ' + ntdsStr + "\n")     
        return True


for t in range(T):
    line = f.readline()    
    line = line.strip()    
    values = line.split()
    N = int(values[0])
    J = int(values[1])

    # print 'N = %d' % N
    # print 'J = %d' % J
    
    j = 0
    
    print 'Case # 1:'
    outFile.write('Case #1:' + "\n")         
    # Generate the combination of bit strings
    bits = ["".join(seq) for seq in itertools.product("01", repeat=N-2)]
    # print bits

    for b in bits:
        coin = []
        coin.append(1)
        for i in range(N-2):
            coin.append(int(b[i]))
        coin.append(1)
        if check(coin):
            j += 1
        if j == J:
            break
    
    



    
        

