import sys
import numpy as np

T = sys.stdin.readline()

def stop_digit(n):
    digits = np.array([False]*10)
    s = 0
    while True:
        s += n
        k = s
        while k > 0:
            digits[k % 10] = True
            k = int(k/10)
        if digits.all():
            break

    return s


case = 1
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        print('Case #%d: INSOMNIA' % case)
    else:
        print('Case #%d: %d' % (case, stop_digit(n)))
    case += 1
