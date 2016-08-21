import sys
if sys.version[0] == '2':
    range, input = xrange, raw_input


def miller_rabin(n):
    """ primality Test
        if n < 3,825,123,056,546,413,051, it is enough to test
        a = 2, 3, 5, 7, 11, 13, 17, 19, and 23.
        Complexity: O(log^3 n)
    """
    assert(n >= 1)
    if n == 2:
        return True
    if n <= 1 or not n & 1:
        return False

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    d = n - 1
    s = 0
    while not d & 1:
        d >>= 1
        s += 1

    for prime in primes:
        if prime >= n:
            continue
        x = pow(prime, d, n)
        if x == 1:
            continue
        for r in range(s):
            if x == n - 1:
                break
            if r + 1 == s:
                return False
            x = x * x % n
    return True


_ = input()
N, J = map(int, input().split())
print("Case #1:")
a = (1 << N-1) + 1
cnt = 0
for b in range(1 << N-2):
    if cnt == J:
        break
    bit = a + (b << 1)
    out = [''.join('1' if bit >> i & 1 else '0' for i in range(N))[::-1]]
    for base in range(2, 11):
        base_num = sum((bit >> i & 1) * pow(base, i) for i in range(N))
        for d in [2, 3, 5, 7, 11]:
            if base_num % d == 0:
                out.append(d)
                break
        else:
            break
    else:
        assert(len(out) == 10)
        print(' '.join(map(str, out)))
        cnt += 1
assert(cnt == J)
