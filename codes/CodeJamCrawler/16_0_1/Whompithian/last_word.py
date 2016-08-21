#!/usr/bin/env python3

import sys

def main():
    output = []
    i = 1
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        a = blank(line)
        output.append('Case #{}: {}\n'.format(i, a))
        i += 1
    with open('output.txt', 'w') as f:
        for o in output:
            f.write(o)

def blank(tc):
    A = [tc[0]]
    for c in tc[1:-1]:
        if c >= A[0]:
            A.insert(0, c)
        else:
            A.append(c)
    return ''.join(A)

if __name__ == "__main__":
    main()
