from __future__ import print_function

import fractions
import sys

def calc(N):
    if N == 0:
        return 'INSOMNIA', 0
    last_number = N
    num_steps = 1

    digits = set()

    while True:
        for ch in str(last_number):
            digits.add(ch)
        if len(digits) == 10:
            break
        last_number = last_number + N
        num_steps += 1
        if num_steps > 1000:
            return 'INSOMNIA', -1

    return last_number, num_steps

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        N = int(f.readline().strip())

        r, _ = calc(N)

        print('Case #{}: {}'.format(case_id, r))

def do_stuff():
    # for i in xrange(1, 201):
    #     n, m = calc(i)
    #     print(i, n, m)

    for i in xrange(1, 10**6 + 1):
        n, m = calc(i)
        if m == -1:
            print(i, n, m)
if __name__ == '__main__':
    main()
    # do_stuff()
