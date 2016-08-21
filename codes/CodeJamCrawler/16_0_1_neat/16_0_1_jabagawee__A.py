#! /usr/bin/env python


def f(n):
    seen = set(str(n))
    current = n
    all_digits = set(map(str, range(10)))
    count = 0
    while all_digits - seen and count < 100:
        current += n
        count += 1
        seen |= set(str(current))
    if all_digits - seen:
        return 'INSOMNIA'
    return current

T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    last_num = f(N)
    print 'Case #{}: {}'.format(i + 1, last_num)
