import pyprimes

it = pyprimes.primes()

def list_primes(n):
    next(it)
    return [next(it) for i in range(n)]

def to_base(n, b):
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n = n // b
    return digits

def in_base(digits, b):
    result = 0
    for d in digits:
        result = b * result + d
    return result

primes = list_primes(200)

def composite(n):
    for p in primes:
        if n % p == 0:
            return p
    return -1

def bases(num):
    return [ in_base(to_base(num, 2), b) for b in range(2, 11) ]

def jamcoin(N, coins):
    num = (2 ** (N-1)) + 1
    while num in coins:
        num += 2

    values = bases(num)
    divisors = []
    
    while (len(divisors) < 9): #loop until we have all divisors
        for v in values:
            div = composite(v)
            if div == -1: # if not composite
                divisors = [] # clear divisors

                num += 2 # try new number
                while num in coins:
                    num += 2

                values = bases(num) # regenerate values
                break
            else:
                divisors.append(div) # add divisor

    coins.append(num)
    print(bin(num)[2:], ' '.join([str(i) for i in divisors]))

T = input()

in_set = input().split()

N = int(in_set[0])
J = int(in_set[1])

coins = []
print('Case #1:')
for j in range(J):
    jamcoin(N, coins)
