#!/usr/bin/env python3
import sys
from concurrent.futures import ThreadPoolExecutor

rl = sys.stdin.readline
if __name__ == "__main__":
    n = int(rl())
    numbers = []

    for i in range(n):
        numbers.append(int(rl().strip()))

    sols = [0 for x in range(100)]
    with ThreadPoolExecutor(max_workers=8) as e:
        def f(case, n):
            history = {}
            seen = set()
            i = 1
            while True:
                _n = n * i
                if _n == 0:
                    sols[case] = -1
                    break
                for v in str(_n):
                    seen.add(v)
                if len(seen) == 10:
                    sols[case] = _n
                    break
                i += 1

        for case, n in enumerate(numbers):
            e.submit(f, case, n)

    for i, sol in enumerate(sols):
        if sol == -1:
            print('Case #%d: INSOMNIA' % (i+1))
        else:
            print('Case #%d: %d' % (i+1, sol))
