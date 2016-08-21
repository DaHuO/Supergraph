#!/usr/bin/env python

import os.path, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="File input", required=True)
    parser.add_argument("-o", "--output", help="File output", required=True)
    args = parser.parse_args()

    lines = list(map(lambda x: x, open(args.input, 'r')))
    T = int(lines[0])

    o = open(args.output, 'w')

    for i in range(1,T+1):
        N = int(lines[i])
        if N == 0:
            o.write("Case #{0}: INSOMNIA\n".format(i))
        else:
            indiv_num = set(list(str(N)))
            current_N = N
            while len(indiv_num) < 10:
                current_N = current_N+N
                indiv_digit_current_N = set(list(str(current_N)))
                indiv_num = indiv_num.union(indiv_digit_current_N)
            o.write("Case #{0}: {1}\n".format(i, current_N))
    o.close()


