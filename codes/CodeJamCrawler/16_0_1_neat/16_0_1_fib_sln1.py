from __future__ import print_function


def sln(n):
    if n == 0:
        return 'INSOMNIA'
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        n_i = i * n
        while n_i:
            digit = n_i % 10
            digits.add(digit)
            n_i //= 10
    return i * n


# for n in xrange(0, 1000001):
#     print(str(n) + ': ' + str(sln(n)))

with open('A-large.in', 'r') as inp, open('ans.txt', 'w') as out:
    T = int(inp.readline())
    case = 0
    for line in inp:
        ans = sln(int(line))
        case += 1
        print('Case #{0}: {1}'.format(case, ans), file=out)
