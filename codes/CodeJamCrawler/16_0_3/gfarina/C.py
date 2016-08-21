import random

def base(n, b):
    ans = 0
    for x in n:
        ans *= b
        if int(x):
            ans += 1
    return ans

def find_divisor(n):
    d = 2
    while d * d <= n and d < n and d <= 500:
        if n % d == 0:
            return d
        d += 1
    return None

assert base('101', 2) == 5
assert base('101', 10) == 101

T = input()
N, J = map(int, raw_input().split())
found = set()

assert T == 1
print "Case #1:"

while len(found) < J:
    test = ['1'] + [random.choice(['0', '1']) for _ in xrange(N - 2)] + ['1']
    divs = [find_divisor(base(test, b)) for b in range(2, 11)]
    #print "testing",test
    teststr = ''.join(test)
    if all(divs) and teststr not in found:
        found.add(teststr)
        print teststr, ' '.join(map(str, divs))
