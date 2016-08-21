
        
def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

primelist = primes2(10 ** 8 + 1)

def factorize(number):
    for prime in primelist:
        if prime > int(number ** 0.5) + 1:
            return -1
        if number % prime == 0:
            return prime
import itertools
import fractions

f = open("C:/C-small.in", "r")
g = open("C:/codejam2016Clarge.txt", "w")
lines = f.readlines()
cases = int(lines[0])

for x in range(1, cases + 1):
    a, b = lines[x].split()
    N = int(a)
    J = int(b)
    
    g.write("Case #%d:\n" % x)
    generated = 0

    generator = itertools.product('10', repeat=N-2)

   # fractions.gcd(.., ..)
    while generated < J:
        next_case = "1%s1" % ''.join(generator.next())
        
        is_prime = True
        factors = ""
        for i in xrange(2, 11):
            in_base = int(next_case, i)
            factorized = factorize(in_base)
            if factorized == -1:
                # PRIME
                is_prime = False
                break
            else:
                # NOT PRIME - GOOD!
                factors += " " + str(factorized)

        if not is_prime:
            continue
        
        g.write('%s%s\n' % (next_case, factors))
        print '%s%s\n' % (next_case, factors)
        generated += 1
            


g.close()
f.close()
