import math
import sys
import itertools

KNOWN_PRIMES = [2]
def is_not_prime(num):
    root = math.sqrt(num)
    if KNOWN_PRIMES[-1] < root:
        grow_known_primes(root)
    for prime in KNOWN_PRIMES:
        if prime > root:
            return False
        if num % prime == 0:
            return prime
    return False

def grow_known_primes(stop):
    i = KNOWN_PRIMES[-1] + 1
    while KNOWN_PRIMES[-1] < stop:
        if not is_not_prime(i):
            KNOWN_PRIMES.append(i)
        i += 1

def prime_or_proof(bitstring):
    proof = []
    for base in range(2, 11):
        num = int(bitstring, base)
        prime_divisor = is_not_prime(num)
        if prime_divisor:
            proof.append(prime_divisor)
        else:
            return False
    return proof


# T = int(sys.stdin.readline())
# for i in range(T):  
#     line = sys.stdin.readline()
#     N, J = [int(x) for x in line.split()]
def find_vals(N,J, i=0):
    count = 0
    print 'Case #%d:' % (i+1)
    for x in itertools.product(['0','1'], repeat=N-2):
        bitstring = '1' + ''.join(x) + '1'
        prime_proof = prime_or_proof(bitstring)
        if prime_proof:
            print bitstring, ' '.join(map(str, prime_proof))
            count += 1  
        if count == J:
            break
