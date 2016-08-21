import os
import re
import sys


def task(S):
    first, middle = 0, 0
    m = re.search(r'(^[-]+)', S, re.MULTILINE)
    if m:
        first = 1

    m = re.findall(r'([+][-])', S)
    if m:
        middle = len(m)

    return first + middle * 2


def main():
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()

    T = int(lines[0])
    res = ''
    for i in range(1, T + 1):
        res += 'Case #%d: %s\n' % (i, task(lines[i]))

    with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as f:
        f.write(res)

if __name__ == '__main__':
    main()
