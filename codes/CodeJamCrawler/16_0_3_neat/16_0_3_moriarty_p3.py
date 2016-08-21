import sys

def tentox(n, b):
    if n == 0:
        return [0]
    d = []
    while n:
        d.append(int(n % b))
        n /= b
    return d[::-1]

def get_decs(n):
    decs = [int(n,i) for i in range(2,11)]
    return decs

def get_candidate_i(N, i):
    bin_num = "{0:b}".format(i)
    return "1"+"0"*(N-len(bin_num))+bin_num+"1"

def is_prime(n):
    if n==2 or n==3: return False
    if n%2==0:
        return False
    if n<2:
        return False
    for i in xrange(3,int((n)**0.5)+1,2):
        if n%i==0:
            return False

    return True

def get_divisors(ls):
    divisors = []
    # print ls
    for x in ls:
        for i in xrange(2,min(sys.maxsize,x)):
            if x % i == 0:
                divisors.append(i)
                break
            # print divisors
    return divisors


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def solve(cipher):
    N, J = map(int,cipher.split())
    # p = set(primes(2**(28)))
    count = 0
    print "Case #1:"
    for i in xrange(2**(N-2)):
        binstr = get_candidate_i(N-2, i)
        decs = get_decs(binstr)
        # print binstr
        # print decs.intersection(p)
        # print decs
        if all([not is_prime(n) for n in decs]):
            # print decs
            print binstr + " " + " ".join(map(str, get_divisors(decs)))
            count+=1
        if count >= J:
            return



if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        solve(cipher)
