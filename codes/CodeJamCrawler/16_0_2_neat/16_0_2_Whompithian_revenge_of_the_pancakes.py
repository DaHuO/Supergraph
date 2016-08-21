#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        a = flip(line)
        output.append('Case #{}: {}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def flip(tc):
    count = 0
    top = tc[0]
    for c in tc[1:-1]:
        if c != top:
            top = c
            count += 1
    if top == '-':
        count += 1
    return count

if __name__ == "__main__":
    main()
