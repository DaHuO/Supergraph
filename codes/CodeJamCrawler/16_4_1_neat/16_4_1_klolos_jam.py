#!/usr/bin/env python

import sys


def allowed():
    a = [(1, 1, 0)]
    for i in range(12):
        v1, v2, v3 = a[-1]
        a.append((v1 + v2, v1 + v3, v2 + v3))

    return a
        

def is_allowed(v1, v2, v3):
    for a in allowed():
        if set((v1, v2, v3)) == set(a):
            return True

    return False


bs = {"P": "PRPS", "R": "PRRS", "S": "PSRS"}

def blocks(v1, v2, v3):
    if v1 + v2 + v3 == 2:
        if v1 == 0:
            return "RS"
        elif v2 == 0:
            return "PS"
        elif v3 == 0:
            return "PR"
    elif v1 + v2 + v3 == 4:
        if v1 == 2:
            return "PRPS"
        elif v2 == 2:
            return "PRRS"
        else:
            return "PSRS"
    elif v1 > v2 and v1 > v3:
        return blocks(v1 / 2, v2 / 2 + 1, v3 / 2) + blocks(v1 / 2, v2 / 2, v3 / 2 + 1)
    elif v2 > v1 and v2 > v3:
        return blocks(v1 / 2 + 1, v2 / 2, v3 / 2) + blocks(v1 / 2, v2 / 2, v3 / 2 + 1)
    elif v3 > v1 and v3 > v2:
        return blocks(v1 / 2 + 1, v2 / 2, v3 / 2) + blocks(v1 / 2, v2 / 2 + 1, v3 / 2)
    elif v3 < v1 and v3 < v2:
        return blocks(v1 / 2 + 1, v2 / 2, v3 / 2) + blocks(v1 / 2, v2 / 2 + 1, v3 / 2)
    elif v2 < v1 and v2 < v3:
        return blocks(v1 / 2 + 1, v2 / 2, v3 / 2) + blocks(v1 / 2, v2 / 2, v3 / 2 + 1)
    elif v1 < v2 and v1 < v3:
        return blocks(v1 / 2, v2 / 2 + 1, v3 / 2) + blocks(v1 / 2, v2 / 2, v3 / 2 + 1)


def solve():
    _, v2, v1, v3 = splitline(int)
    if not is_allowed(v1, v2, v3):
        return "IMPOSSIBLE"

    return blocks(v1, v2, v3)


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(f):
    return map(f, readline().split())


def main():
    for i in range(int(readline())):
        print_result(solve(), i + 1)


if __name__ == '__main__':
    main()
