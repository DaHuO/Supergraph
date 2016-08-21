from math import sqrt, ceil

# eg
N = 6
J = 3

# small
N = 16
J = 50

# large
N = 32
J = 500

# check only factors < m
def is_prime(n, m):
    N = int(ceil(sqrt(n)))
    N = min(m, n)
    for i in xrange(3, N):
        if n % i == 0:
            return i
    return -1

def solve(string):
    cc = [0] * 9
    for i in xrange(2, 11):
        c = is_prime(int(string, i), 1000)
        if c == -1:
            return None
        else:
            cc[i - 2] = c
    return cc

print('Case #1:')

n = 2**(N - 1) + 1
while J > 0:
    string = bin(n)[2:]
    cc = solve(string)
    if cc != None:
        print '%s %s' % (string, ' '.join(map(str, cc)))
        J -= 1
    n += 2
