#!/usr/bin/env python

def get_min_number(N):
    if N == 0:
        return 'INSOMNIA'

    seen = [0] * 10
    c = 1
    while True:
        t = N * c
        while t:
            seen[t % 10] = 1
            t /= 10

        done = True
        for i in range(10):
            if seen[i] == 0:
                done = False
        if done:
            return N * c
        c += 1

if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        N = int(raw_input())
        print 'Case #%d: %s' % (tc, get_min_number(N))
