from math import ceil, sqrt
from random import randint

BASES = range(2,11)

def interpret(n):
    return map(lambda x : base(n, x), BASES)

def base(n, b):
    result = 0
    e = 0
    while n > 0:
        if n%10 == 1:
            result += b**e
        e += 1
        n /= 10
    return result

def is_prime(n):
    if n == 0 or n == 1:
        return False
    # Check small primes
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n)))+1, 2):
        if n % i == 0:
            return False
    return True

def divisors(n):
    for i in range(3, int(ceil(sqrt(n)))+1, 2):
        if n%i == 0:
            yield n / i
            yield i

def is_jamcoin(nums):
    return all(map(lambda n : not(is_prime(n)), nums))

def make_candidate(n):
    l = n - 2
    result = 10
    for i in xrange(0, l):
        result += randint(0, 1)
        result *= 10
    result += 1
    return result

def test():
    assert(is_prime(2))
    assert(is_prime(3))
    assert(is_prime(5))
    assert(is_prime(7))
    assert(is_prime(11))
    assert(is_prime(13))
    assert(is_prime(17))
    assert(is_prime(6199))

    assert(is_prime(9) == False)
    assert(is_prime(123456782) == False)
    assert(is_prime(1782) == False)
    assert(is_prime(21) == False)
    assert(is_prime(25) == False)
    assert(is_prime(15) == False)

    assert(is_jamcoin(interpret(100011)))
    assert(is_jamcoin(interpret(111111)))
    assert(is_jamcoin(interpret(111001)))
    assert(not(is_jamcoin(interpret(110111))))

    for b in range(1, 12):
        assert(base(1, b) == 1)
    for b in range(0, 11):
        for e in range(0, 33):
            assert(base(10 ** e, b) == b**e)

    for l in range(2, 50):
        c = str(make_candidate(l))
        assert(len(c) == l)
        assert(c[0] == '1')
        assert(c[-1] == '1')
        assert(all(map(lambda x : x == '0' or x == '1', c)))

def solve(length, j):
    found = 0
    while found != j:
        c = make_candidate(length)
        nums = interpret(c)
        if not(is_jamcoin(nums)):
            continue
        used = []
        seen = set()
        for n in nums:
            for d in divisors(n):
                if d not in seen:
                    used.append(d)
                    seen.update({d})
                    break
        if len(used) == 9:
            found += 1
            print str(c) + ' ' + ' '.join(map(str,used))

if __name__ == '__main__':
    test()
    T = int(raw_input())
    line = raw_input()
    N, J  = map(int, line.split(' '))
    print  ('Case #1:')
    solve(N, J)
