import sys
from math import sqrt; from itertools import count, islice

cnt = 0 # lazy, kill me

def generate(j, i):
    # Converting to bin gives the base:
    # 3 -> 101  -> 2^2 + 1 = 5
    # 4 -> 1001 -> 2^3 + 1 = 9
    number = pow(2, j - 1) + 1
    # Add incrementer shifted left
    number = number + i * 2
    if number > pow(2, j):
        print("DANGER, number overflow")
    return "{0:b}".format(number)

def get_bases(coinjam):
    bases = {}
    for i in xrange(2, 11): # 10 included
        bases[i] = int(coinjam, base=i)
    return bases

def is_prime(num):
    # Rationality behind semi optimized pythonic prime checking:
    # http://stackoverflow.com/a/27946768/552214
    if num < 2: 
        return False
    for n in islice(count(2), int(sqrt(num) - 1)):
        if not num % n:
            return False

    return True

def check_prime(bases):
    # Check if all bases are not prime
    checks = [is_prime(bases[num]) for num in bases]
    #print(checks)
    return not any(checks)


def get_divisor(num):
    # Similar to prime checking
    for n in islice(count(2), int(sqrt(num) - 1)):
        if not num % n:
            return n
    # This should never be reached, else leave it to None just to know there's problems

def get_divisors(bases):
    divisors = []
    for b in bases:
        divisors.append(get_divisor(bases[b]))
    return divisors

def verify(j):
    '''
    1. Generate coinjam
    2. Get bases
    3. Verify they're not prime
    4. Get nontrivial divisor
    '''
    global cnt
    coinjam = None
    while not coinjam:
        tmp = generate(j, cnt)
        cnt = cnt + 1
        bases = get_bases(tmp)
        #print(j, cnt, tmp, bases)
        # Check if there are NO primes
        if check_prime(bases):
            coinjam = tmp
            divisors = get_divisors(bases)
            #print("COINJAM", tmp, divisors)
            return coinjam, divisors

    return None


if __name__ == '__main__':
    J = 16
    N = 50
    output = []
    output.append("Case #1:")
    for i in xrange(N):
        print(i)
        coinjam, divisors = verify(J)
        divisors = ' '.join(str(d) for d in divisors)
        output.append("{0} {1}".format(coinjam, divisors))

    with open('output', 'w') as f:
        f.write('\n'.join(output))