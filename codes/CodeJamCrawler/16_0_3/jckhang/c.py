import numpy as np


def coin(n, j):
    suc = 0
    print('Case #1:')
    for num in range(1 << n - 2):
        if suc == j:
            return
        else:
            s = bin(num)[2:]
            s = '0' * (n - 2 - len(s)) + s
            st = '1' + str(s) + '1'
            prime = []
            numbers = []
            for i in range(2, 11):
                number = int(st, i)
                numbers.append(number)
                low = 3
                upper = 10000
                for div in range(low, upper):
                    if number % div == 0:
                        prime.append(div)
                        break
            if len(prime) == 9:
                print('{} {}'.format(st, ' '.join(map(str, prime))))
                suc += 1

t = int(raw_input())
for i in xrange(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]
    coin(n, j)
