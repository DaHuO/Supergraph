import sys
import random

all_primes = map(int, open('65.txt').readlines())


def bin(a):
    s = ''
    t = {'0': '000', '1': '001', '2': '010', '3': '011',
         '4': '100', '5': '101', '6': '110', '7': '111'}
    for c in oct(a)[1:]:
        s += t[c]
    return s


def get_factor(n):

    for f in all_primes:
        if n % f == 0:
            return f

    return 0

T = int(sys.stdin.next())
[N, J] = map(int, sys.stdin.next().split(' '))

success = set([])

print('Case #1:')
while J > 0:
    s = random.randint(2 ** (N - 1), 2 ** N - 1)
    s = bin(s)[-N:]
    s = s[:-1] + '1'

    if s in success:
        continue

    factors = []
    fail = False
    for b in range(2, 11):
        i = int(s, b)
        f = get_factor(i)
        factors.append(f)
        if f == 0:
            fail = True
            break
    if fail:
        continue
    else:
        print(s + ' ' + ' '.join(map(str, factors)))
        success.add(s)
        J -= 1
