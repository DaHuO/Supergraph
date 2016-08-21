from __future__ import print_function

import fractions
import sys

def calc(K, C, S):
    if S < K:
        return 'IMPOSSIBLE'
    return list(range(1, K+1))

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        K, C, S =  map(int, f.readline().strip().split())

        r = calc(K, C, S)
        r_str = r if isinstance(r, str) else str.join(' ', map(str, r))

        print('Case #{}: {}'.format(case_id, r_str))

if __name__ == '__main__':
    main()
