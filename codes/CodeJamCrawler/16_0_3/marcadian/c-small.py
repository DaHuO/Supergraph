
def get_value(binary, base):
    v = 1
    ret = 0
    for c in binary[::-1]:
        if c == '1':
            ret += v
        v *= base
    return ret


def get_divisor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return None

n = 16
j = 50

print "Case #1:"
ret = 0
import itertools
for num in itertools.product('01', repeat=n):
    binary = ''.join(num)
    if binary[0] != '1' or binary[-1] != '1':
        continue
    divisors = []
    for base in xrange(2, 11):
        v = get_value(binary, base)
        divisor = get_divisor(v)
        if divisor:
            divisors.append(str(divisor))
        else:
            break
    if len(divisors) == 9:
        print binary, ' '.join(divisors)
        ret += 1
        if ret == j:
            break
