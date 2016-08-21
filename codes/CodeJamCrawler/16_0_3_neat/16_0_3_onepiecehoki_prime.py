primes = []

def generate_primes(upper_bound=1000000):
    # Implement Euler's Sieve
    global primes
    primes.append(2)
    buff = [2*i+1 for i in xrange(1,(upper_bound-1)/2)]
    cur_prime = 2
    sqrt_upper_bound = int(upper_bound ** 0.5)+1
    while cur_prime < sqrt_upper_bound:
        cur_prime = buff[0]
        buff = [i for i in buff if i%cur_prime != 0]
        primes.append(cur_prime)
    primes += buff
    return primes

#Check whether the number is a prime until the square of the largest prime in primes
def is_prime(x):
    global primes
    if x <= 1:
        return False
    elif len(primes) == 0:
        generate_primes(100000)
    for p in primes:
        if x%p == 0:
            return False
        if p*p > x:
            return True
    return True

def prime_factor(x):
    global primes
    if x <= 1:
        return []
    if len(primes) == 0:
        generate_primes(100000)
    factors = []
    for p in primes:
        pow = 0
        while x%p == 0:
            pow+=1
            x/=p
        if pow > 0:
            factors.append((p,pow))
        if p*p > x:
            break
    if x > 1:
        factors.append((x,1))
    return factors

if __name__ == '__main__':
    print(generate_primes(103))


