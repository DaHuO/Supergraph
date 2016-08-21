
def helper(n, s):
    if n == 0:
        return s
    s.update({n%10})
    return helper(n/10, s)

def digits(n):
    return helper(n, set())

def brute(n):
    seen = set()
    seen.update(digits(n))
    i = 1
    while len(seen) != 10:
        i += 1
        seen.update(digits(n*i))
    return i

rng = range(1, 10**6+1)
ans = None

def solve(n):
    global ans
    if ans == None:
        ans = dict(zip(rng, map(brute, rng)))
    if n == 0:
        return 'INSOMNIA'
    return n * ans[n]

def test():
    assert(digits(1) == {1})
    assert(digits(3) == {3})
    assert(digits(11111) == {1})
    assert(digits(12) == {1, 2})
    assert(digits(123) == {1, 2, 3})
    assert(digits(1234) == {1, 2, 3, 4})
    assert(digits(12345) == {1, 2, 3, 4, 5})
    assert(digits(123546) == {1, 2, 3, 4, 5, 6})
    assert(digits(1234567) == {1, 2, 3, 4, 5, 6, 7})
    assert(digits(12345678) == {1, 2, 3, 4, 5, 6, 7, 8})
    assert(digits(123456789) == {1, 2, 3, 4, 5, 6, 7, 8, 9})
    assert(digits(1234567890) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 0})
    assert(digits(1222234567890) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 0})
    assert(digits(1222000234567890) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 0})
    assert(digits(1) == {1})
    assert(digits(3) == {3})

    assert(brute(1) == 10)
    assert(brute(2) == 45)
    assert(brute(3) == 10)
    assert(brute(4) == 23)
    assert(brute(5) == 18)
    assert(brute(6) == 15)
    assert(brute(7) == 10)
    assert(brute(8) == 12)
    assert(brute(9) == 10)

    assert(solve(0) == 'INSOMNIA')
    assert(solve(1) == 10)
    assert(solve(2) == 90)
    assert(solve(11) == 110)
    assert(solve(1692) == 5076)

if __name__ == '__main__':
    test()
    T = int(raw_input())
    for n in range(1, T+1):
        s = solve(int(raw_input()))
        print('Case #{}: {}'.format(n, s))
