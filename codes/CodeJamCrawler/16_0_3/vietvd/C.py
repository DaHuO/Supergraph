def is_prime(n):
    """check number n is prime"""

    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False

    return True


def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    n = 0
    for d in digits:
        n = b * n + int(d)
    return n

ifile = open('C-small-attempt0.in', 'r')
ofile = open('C.test.out', 'w')

TC = int(ifile.readline())
[N, J] = [int(i) for i in ifile.readline().split(' ')]
start = 2 ** (N - 1)
count = 0

out = "Case #1:\n"

while(count < J):
    digit = bin(start)[2:]
    if digit[-1] == '0' or digit[0] == '0':
        start += 1
        continue
    ok = True
    nbs = []
    for b in xrange(2, 11):
        nb = fromDigits(digit, b)
        nbs.append(nb)
        if is_prime(nb):
            ok = False
            break

    if ok:
        count += 1
        out += "%s " % digit
        for nb in nbs:
            for j in xrange(2, nb):
                if nb % j == 0:
                    out += "%d " % j
                    break
        out += "\n"
    start += 1

ofile.write(out)
