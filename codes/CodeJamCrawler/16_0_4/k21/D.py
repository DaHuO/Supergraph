#!/usr/bin/env python3

T = int(input())
for t in range(T):
    print('Case #{}:'.format(t+1), end='')
    K, C, S = map(int, input().split())
    if K != S: continue
    for i in range(K):
        print(' {}'.format(i+1), end='')
    print()
