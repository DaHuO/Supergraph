import sys

import numpy as np

def interpret_in_bases(cj, base=2):
    n = len(cj)
    cj = [int(c) for c in cj]
    factors = [base**i for i in range(n)][::-1]

    return sum(c*f for c,f in zip(cj, factors))


def generate_primes(n=2**16):

    return primes

def generate_prims(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)       ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def count(inputline):
    orgnumber = int(inputline)
    if orgnumber==0:
        return "INSOMNIA"
    
    # find max digit
    seendigits = set()
    n = 0
    while len(seendigits)<10:
        n += 1
        number = n*orgnumber
        digits = getdigits(number)
        for d in digits:
            seendigits.add(d)

    return "{}".format(number)

def is_jamcoin(i, primes):
    s = bin(i)[2:]
    if s[-1]=="0":
        return False
    print(s)
    factors = [s]
    for b in [2,3,4,5,6,7,8,9,10]:
        interpretation = interpret_in_bases(s, b)
        # cancel if prime
        if interpretation in primes:
            return False
        # find factor
        factor = 0
        for p in primes:
            if interpretation % p == 0:
                factor = p
                break
        if factor != 0:
            factors.append(str(factor))

        else:
            return False

    return factors



if "__main__" == __name__:
    inp = sys.argv[1]
    print(inp)
    if inp=="test":
        N, J = 6, 3
    elif inp=="small":
        N, J = 16, 50
    elif inp=="large":
        N, J = 32, 500

    primes = generate_prims(2**N)


    out = []
    i = 2**(N-1)+1
    while len(out)<J:
        ret = is_jamcoin(i, primes)
        if ret:
            out.append(ret)
        i = i+1

    
    with open("out_"+inp, 'w') as f:
        f.write("Case #1:\n")
        for o in out:
            f.write(" ".join(o))
            f.write("\n")
            print(o)
    print(out)