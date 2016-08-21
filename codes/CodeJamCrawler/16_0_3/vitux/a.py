# -*- coding: utf-8 -*-


def is_prime(n):
    if n == 2 or n == 3:
        return 0
    if n < 2 or n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return f
        if n % (f + 2) == 0:
            return f + 2
        f += 6
    return 0

i = 2 ** 15 + 1
ans = []
while len(ans) < 50:
    curr = bin(i)[2:]
    kek = []
    for base in xrange(2, 11):
        d = is_prime(int(curr, base))
        if d == 0:
            break
        kek.append(d)
    else:
        ans.append((curr, kek))
    i += 2
print 'Case # 1:'
for i, k in ans:
    print i, ' '.join(map(str, k))