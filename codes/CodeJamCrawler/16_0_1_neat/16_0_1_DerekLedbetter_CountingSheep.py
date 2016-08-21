#!/usr/bin/env python3

T = int(input().strip())

for i in range(1, T + 1):
    N = int(input().strip())
    if N != 0:
        digitsFound = [ False ] * 10
        m = N
        while True:
            for digit in str(m):
                digitsFound[int(digit)] = True
            if all(digitsFound):
                break
            m += N
        answer = str(m)
    else:
        answer = 'INSOMNIA'
    print('Case #{}: {}'.format(i, answer))

