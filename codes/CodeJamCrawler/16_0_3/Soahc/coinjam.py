import random

def modPow(a, b, m):
    v = 1
    p = a % m
    while b > 0:
        if (b & 1) != 0:
            v = (v * p) % m
        p = (p * p) % m
        b >>= 1
    return v
 
def witness(a, n):
    n1 = n - 1
    s2 = n1 & -n1
    x = modPow(a, n1 / s2, n)
    fact = gcd(x - 1, n)
    if x == 1 or x == n1:
        return 1
    while s2 > 1:
        x = (x * x) % n
        if x == 1:
            return fact
        if x == n1:
            return 1
        s2 >>= 1
    return fact

def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def searchFactor(n, k):
    fact = 1
    if n > 5:
        for i in xrange(k):
            fact = witness(random.randint(2, n - 1), n)
            if fact != 1:
                break
    return fact

def coinjam(N, J, k):
    bits = [1] + [0]*(N-2) + [1]
    while J > 0:
        out = ''.join([str(b) for b in reversed(bits)])
        for base in xrange(2, 10 + 1):
            num = 0
            acc = 1
            for b in bits:
                if b:
                    num += acc
                acc *= base
            fact = searchFactor(num, k)
            if fact != 1:
                out += ' ' + str(fact)
            else:
                out = None
                break
        if out != None:
            print out
            J -= 1
        # add bits
        for i in xrange(1, N-1):
            if bits[i] == 1:
                bits[i] = 0
            else:
                bits[i] = 1
                break
        if bits.count(0) == (N-2):
            break

if __name__ == '__main__':
    t = int(raw_input())
    ci = 1
    for i in xrange(1, t + 1):
        n, m = [int(s) for s in raw_input().split(" ")]
        print 'Case #{}:'.format(i)
        coinjam(n, m, 100)
