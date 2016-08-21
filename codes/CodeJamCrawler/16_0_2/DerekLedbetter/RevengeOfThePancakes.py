#!/usr/bin/env python3

T = int(input().strip())

for i in range(1, T + 1):
    S = input().strip()
    assert all(ch in '+-' for ch in S)

    answer = 0
    previous = '+'
    for ch in reversed(S):
        if previous != ch:
            answer += 1
        previous = ch
    print('Case #{}: {}'.format(i, answer))
