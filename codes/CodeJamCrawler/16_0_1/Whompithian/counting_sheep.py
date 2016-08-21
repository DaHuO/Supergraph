#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        a = last_num(line)
        output.append('Case #{}: {}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def last_num(tc):
    done = False
    base = 0
    A = int(tc)
    seen = set()
    if not A:
        return 'INSOMNIA'
    while not done:
        base += A
        temp = base
        while temp:
            seen.add(temp % 10)
            temp //= 10
        done = len(seen) == 10
    return base

if __name__ == "__main__":
    main()
