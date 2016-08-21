def base(s, b):
    acc = 0
    for c in s:
        acc = acc * b + (c == '1')
    return acc

def factor(n):
    from math import floor
    if n < 4:
        return 0
    if n%2 == 0:
        return 2
    for d in range(3, 10000, 2):
        if n%d == 0:
            return d
    # too much work to determine if it's composite
    return 0

import fileinput

f = fileinput.input()
T = int(f.readline())
[N, J] = map(int, f.readline().split())

print('Case #1:')

n = 1 + 2**(N-1)
j = 0
while j < J:
    s = bin(n)[2:]
    factors = []
    for b in range(2, 11):
        x = base(s, b)
        f = factor(x)
        if f:
            factors.append(f)
        else:
            break
    if len(factors) == 9:
        output = s + ' ' + ' '.join(map(str, factors))
        print(output)
        j += 1
    n += 2
