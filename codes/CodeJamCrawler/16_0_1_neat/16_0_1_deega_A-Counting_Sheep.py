#!/bin/python
T = int(input())
for i in range(T):
    N = int(input())
    v = set()
    M = N
    c = 0
    j = 1
    while True:
        if N == 0:
            break
        if len(v) == 10:
            break
        M = j * N
        temp = set(str(M))
        v |= temp
        c += 1
        j += 1
    res = M if len(v) == 10 else 'INSOMNIA'
    print('Case #{}: {}'.format(i+1,res))
