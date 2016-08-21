#! /usr/bin/env python


def ith_spot(i, k, c):
    if c == 1:
        return i
    chunk_size = k ** (c - 1)
    return (i - 1) * chunk_size + ith_spot(i, k, c - 1)

T = int(raw_input())
for c in range(T):
    K, C, S = map(int, raw_input().split())
    spots = [ith_spot(i, K, C) for i in range(1, K+1)]
    print 'Case #{}: {}'.format(c + 1, ' '.join(map(str, spots)))
