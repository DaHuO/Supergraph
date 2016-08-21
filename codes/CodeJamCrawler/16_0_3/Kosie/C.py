#!/usr/bin/env python3

T = int(input())

for case in range(1, T+1):
    print('Case #{}:'.format(case))

    N, J= map(int, input().split())
    assert N % 2 == 0, 'N must be even'

    for j in range(J):
        number = '1{{:0{}b}}'.format(N//2 - 1).format(j)
        number = number + number[::-1]
        answer = [number]
        for base in range(2, 11):
            val = int(number, base) + 1
            assert val % (base + 1) == 0, 'val must be divisible by base+1'
            answer.append(base + 1)
        print(' '.join(map(str, answer)))
