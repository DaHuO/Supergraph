#!/usr/bin/env python3

T = int(input())

def update_seen(seen, val):
    for d in str(val):
        seen[int(d)] = True

for case in range(1, T+1):
    answer = "INSOMNIA"
    N = int(input())

    seen = [False] * 10
    if N != 0:        
        multi = 0
        while not all(seen):
            multi += 1
            update_seen(seen, N * multi)
        answer = multi * N

    print('Case #{}: {}'.format(case, answer))
