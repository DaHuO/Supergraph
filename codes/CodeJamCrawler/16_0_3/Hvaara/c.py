primes = []

def gen_jamcoin(n):
    m = n-2
    for i in xrange(2**(m)):
        yield "1{0:0{width}}1".format(int("{0:b}".format(i)), width=m)

def sieve(n):
    """We want all primes up to n"""
    bits = [True]*(n+1)
    bits[0] = False
    bits[1] = False
    for i in range(2, n+1):
        if bits[i]:
            j = 2
            while i*j <= n:
                bits[i*j] = False
                j += 1
    for i in range(n+1):
        if bits[i]:
            primes.append(i)

def check_prime(coin):
    for prime in primes:
        if coin%prime == 0 and prime != coin:
            return prime
    return False

def check_valid(coin):
    out = []
    for base in range(2, 11):
        cur = int(coin, base)
        val = check_prime(cur)
        if not val:
            return False
        out.append(val)
    return out

def write(filename, out):
    with open(filename, 'w') as f:
        f.write("Case #1:\n")
        f.write("\n".join(out))
        f.write("\n")

if __name__ == '__main__':
    import sys
    max_prime = 10000
    n = int(sys.argv[1])
    j = int(sys.argv[2])
    out = []
    outname = "{0}-{1}.out".format(n, j)

    sieve(max_prime)
    for i in gen_jamcoin(n):
        val = check_valid(i)
        if val:
            out.append(str(i) + " " + " ".join(str(x) for x in val))
            if len(out) == j:
                break
    write(outname, out)
