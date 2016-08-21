#!/usr/bin/env python3

def seen_all(s):
    return set('0123456789') - s == set()

T = int(input())
for i in range(1, T + 1):
    N = input()
    seen = set(N)
    prev = N = int(N)
    while prev and not seen_all(seen):
        seen |= set(str(prev))
        prev += N
    print("Case #{}: {}".format(i, prev - N if prev - N > 0 else 'INSOMNIA'))
