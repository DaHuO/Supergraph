N = 16
J = 500
primes = [2]
for i in xrange(3, 100):
    is_prime = True
    for j in xrange(2, i):
        if i % j == 0:
            is_prime = False
            break
        if j * j > i:
            break
    if is_prime:
        primes.append(i)

def to_int(s, base):
    global N
    res = 0
    for i in xrange(N):
        res += (base ** (N - i - 1)) * int(s[i])
    #print s, base, res
    #raw_input()
    return res

def dfs(dep, digit):
    global N, primes, J
    if dep < N:
        dfs(dep + 1, digit + '0')
        dfs(dep + 1, digit + '1')
    else:
        if digit[-1] == '0':
            return
        cnt = 0
        res = []
        for i in xrange(2, 11):
            num = to_int(digit, i)
            #print num
            ok = False
            for prime in primes:
                #print num, prime
                if num % prime == 0:
                    res.append(prime)
                    ok = True
                    break
            if not ok:
                return
        if J:
            J -= 1
            print digit + digit, ' '.join(map(str, res))
dfs(1, '1')
