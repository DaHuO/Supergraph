import random
ZERO = ord('0')


def find_divisor(num):
    for i in range(2, min(num - 1, 1000)):
        if num % i == 0:
            return i
    return None


def test(s):
    ret = []
    for base in range(2, 11):
        num = 0
        for i in range(len(s)):
            num += base ** (len(s) - i - 1) * (ord(s[i]) - ZERO)
        divisor = find_divisor(num)
        if divisor:
            ret.append(divisor)
        else:
            return None
    return ret


def random_string(n):
    ret = '1'
    for i in range(n - 2):
        ret += chr(random.randint(0, 1) + ZERO)
    ret += '1'
    return ret


used = set()
n = 32
j = 500
print 'Case #1:'
while len(used) < j:
    s = random_string(n)
    if s in used:
        continue
    divs = test(s)
    if divs:
        used.add(s)
        ret = s
        for div in divs:
            ret += ' {}'.format(div)
        print ret
