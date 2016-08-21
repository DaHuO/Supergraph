#!/usr/bin/env python3

T = int(input())
for t in range(T):
    print('Case #{}: '.format(t+1), end='')
    N = int(input())
    if N == 0:
        print('INSOMNIA')
        continue
    k = 0
    seen_digits = set()
    while len(seen_digits) < 10:
        k += 1
        m = N * k
        seen_digits.update(str(m))
    print(N * k)
