import math

def rint():
    return int(rstr())

def rints_line():
    return [int(s) for s in rstr().split()]

def rstr():
    return input()

def gen_candidates(n):
    _n = n - 2
    if _n > 1:
        fstr = '1{{:0>{}}}1'.format(_n)
        for x in range(2 ** _n):
            yield fstr.format(bin(x)[2:])
    elif n == 2:
        yield from ['11']

def candidate_reps(candidate):
    return [int(candidate, base) for base in range(2, 11)]

def rwh_primes2(n):
    """
    Input n>=6, Returns a list of primes, 2 <= p < n
    http://stackoverflow.com/a/2068548/847552
    """
    correction = n % 6 > 1
    n = {0: n, 1: n-1, 2: n+4, 3: n+3, 4: n+2, 5: n+1}[n % 6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k=3*i + 1|1
            sieve[      ((k*k)//3)      ::2*k] = [False] * ((n//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = [False] * ((n//6 - (k*k + 4*k - 2*k*(i&1))//6 - 1)//k + 1)
    return [3] + [3*i+1|1 for i in range(1, n//3 - correction) if sieve[i]]

def find_div(n):
    i = 0
    lim = int(math.sqrt(n) + 1)
    while True:
        try:
            p = primes[i]
        except IndexError:
            return
        if p > lim:
            return
        if n % p == 0:
            return p
        i += 1

def find_divs(reps):
    divs = []
    for rep in reps:
        d = find_div(rep)
        if not d:
            return
        divs.append(d)
    return divs

def solve(N, J):
    jamcoins = {}
    for c in gen_candidates(N):
        reps = candidate_reps(c)
        if primes_set.intersection(reps):
            continue
        divs = find_divs(reps)
        if not divs:
            continue
        jamcoins[c] = divs
        if len(jamcoins) >= J:
            break

    return jamcoins

def out(jamcoins):
    print('Case #1:')
    for jc, divs in jamcoins.items():
        print(jc, ' '.join(str(d) for d in divs))

if __name__ == '__main__':
    T = rint()
    N, J = rints_line()
    primes = rwh_primes2(2 ** (N // 2) + 1)
    primes_set = set(primes)
    jamcoins = solve(N, J)
    out(jamcoins)

