#! /usr/bin/env python3

from collections import deque

T = int(input())

for t in range(1, T+1):
    s = input()
    deq = deque()
    deq.append(s[0])
    for c in s[1:]:
        for ch in deq:
            if c > ch:
                deq.appendleft(c)
                break
            elif c < ch:
                deq.append(c)
                break
        else:
            deq.append(c)

    print('Case #{}: {}'.format(t, ''.join(deq)))
