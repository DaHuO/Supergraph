#!/usr/bin/env python3

T = int(input().strip())

for i in range(1, T + 1):
    K, C, S = [ int(x) for x in input().split() ]
    if C * S >= K:
        # Find S numbers of base K and length C such that each digit is used
        # at least once in one of the numbers, then add 1.
        result = []
        firstDigit = 0
        while firstDigit < K:
            n = 0
            for d in range(firstDigit, firstDigit + C):
                n = K * n + min(d, K - 1)
            n += 1
            result.append(n)
            firstDigit += C
        assert len(result) <= S
        answer = ' '.join(str(n) for n in result)
    else:
        answer = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(i, answer))
