import sys
import numpy

# this method is from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n (thanks a lot!)
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def iterator(n):
    i = 0
    while i < n:
        yield i
        i += 1

def candidates(n):
    # prepare list
    nums = []
    nums.append(1)
    for i in iterator(n - 2):
        nums.append(0)
    nums.append(1)
    # number of possibilities = 2^(n-2)
    possibilities = 1
    for i in iterator(n - 2):
        possibilities *= 2
    # generate candidates
    for i in iterator(possibilities):
        yield nums
        nums[-2] += 1
        for k in range(1, n - 1):
            if nums[-k] == 2:
                nums[-k] = 0
                nums[-k-1] += 1

def interpret_mod(nums, base, d):
    x = 0
    m = 1
    for i in iterator(len(nums)):
        x += (nums[-i-1] * (m % d)) % d
        x %= d
        m *= base
    return x

def divisor(nums, base, prime_max):
    if interpret_mod(nums, base, 2) == 0:
        return 2
    for d in primesfrom2to(prime_max):
        remainder = interpret_mod(nums, base, d)
        if remainder == 0:
            return d
    return 1

def check(nums, prime_max):
    divisors = []
    for base in range(2, 11):
        #x = interpret(nums, base)
        d = divisor(nums, base, prime_max)
        if d == 1:
            return False
        divisors.append(d)
    # output
    outstr = ""
    for c in nums:
        outstr += str(c)
    for d in divisors:
        outstr += " " + str(d)
    print(outstr)
    return True

def main():
    print("Case #1:")
    # settings:
    n = int(sys.argv[1])
    j = int(sys.argv[2])
    prime_max = 8
    # end settings
    # begin algorithm
    k = 0
    for candidate in candidates(n):
        if check(candidate, prime_max):
            k += 1
            if k == j:
                return
    if k != j:
        print("DID NOT FIND ENOUGH COINS!")

if __name__ == "__main__":
    main()
