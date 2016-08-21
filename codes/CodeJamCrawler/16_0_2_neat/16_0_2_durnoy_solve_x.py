from __future__ import print_function

import fractions
import sys

def calc(S):
    num_flips = 0
    i = 0

    while True:
        while i < len(S) and S[i] == '+':
            i += 1
        if i >= len(S):
            break
        j = i
        while j < len(S) and S[j] == '-':
            j += 1
        if i > 0:
            num_flips += 1
        num_flips += 1
        i = j

    return num_flips

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        S =  f.readline().strip()

        r = calc(S)

        print('Case #{}: {}'.format(case_id, r))

if __name__ == '__main__':
    main()
