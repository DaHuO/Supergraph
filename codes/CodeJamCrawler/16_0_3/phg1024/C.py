def to_binary(i, N):
    s = []
    while N>0:
        d = i % 2
        i = i / 2
        s.append(str(d))
        N -= 1
    return ''.join(s[::-1])

def interpret(s, base):
    val = 0
    for d in s:
        val *= base
        val += int(d) * base
    return val / base

def gen_primes(N):
    is_prime = [True for i in range(N+1)]
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    max_i = int(N**0.5) + 1
    i = 2
    while True:
        j = i * 2
        while j <= N:
            is_prime[j] = False
            j += i
        while i < max_i:
            i += 1
            if is_prime[i]:
                break

        if i >= max_i:
            break
    return [i for i in range(N+1) if is_prime[i]], is_prime

def factorize(val, primes):
    i = 0
    factors = []
    q = 1
    while val > 0 and i < len(primes):
        #print val, i
        is_factor = False
        while True:
            if val % primes[i] == 0:
                is_factor = True
                val /= primes[i]
                q *= primes[i]
            else:
                break
        if is_factor:
            factors.append(primes[i])
        i += 1
    if factors:
        return factors
    else:
        return []

def test(i, N, primes, is_prime):
    s = to_binary(i, N)
    factors = []
    for b in range(2, 11):
        val = interpret(s, b)
        f = factorize(val, primes)
        if f:
            if f[0] == val:
                return []
            else:
                factors.append(f[0])
        else:
            return []
    return (s, factors)

def solve(N, J, primes, is_prime):
    count = 0
    i = 2**(N-1) + 1
    i_max = 2**N - 1
    while count < J and i<i_max:
        res = test(i, N, primes, is_prime)
        if res:
            count += 1
            x, d = res
            print '%s %d %d %d %d %d %d %d %d %d' % (x, d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8])
        i += 2

if __name__ == '__main__':
    primes, is_prime = gen_primes(2**16+1)

    T = int(raw_input())

    for i in range(T):
        N, J = map(int, raw_input().split())
        print 'Case #%d:' % (i+1)
        solve(N, J, primes, is_prime)