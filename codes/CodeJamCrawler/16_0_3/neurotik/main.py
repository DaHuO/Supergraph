import math
from math import sqrt; from itertools import count, islice

def read_int():
    return int(fi.readline())

def read_intlist():
    return [int(i) for i in fi.readline().split(' ')]

def write_line(i, s):
    fo.write('Case #%d: %s\n' % (i+1, s))

def read_str():
    return fi.readline().strip('\n')

filename = 'C-small-attempt0'
fi = file(filename + '.in', 'rb')
fo = file(filename + '.out', 'wb')


def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def jamcoin(s):
    div = []
    for i in range(2, 11):
        n = int(s, i)
        if is_prime(n):
            return False

    for i in range(2, 11):
        n = int(s, i)
        for i in xrange(2, n/2):
            if n % i == 0:
                div.append(str(i))
                break

    return '%s %s' % (s, ' '.join(div))


T = read_int()
n, j = read_intlist()
c = 0

fo.write('Case #1:\n')
for i in xrange(int(math.pow(2, n-2))):
    s = str_base(i, 2)
    if len(s) < n-2:
        s = '0'*(n-2-len(s)) + s
    s = '1%s1' % s

    jc = jamcoin(s)
    if jc:
        fo.write(jc + '\n')
        c = c + 1
        if c == j: break


fi.close()
fo.close()