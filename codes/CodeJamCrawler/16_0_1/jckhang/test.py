import numpy as np


def count_sheep(n):
    digits = np.zeros((10,), dtype=bool)
    t = 0
    now = n
    while (t < 100) and (sum(digits) < 10):
        number = now
        while number:
            digit = number % 10
            digits[digit] = True
            number //= 10
        now += n
        t += 1
    if sum(digits) == 10:
        return now - n
    else:
        return 'INSOMNIA'

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    result = count_sheep(n)
    print "Case #{}: {}".format(i, result)
