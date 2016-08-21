#!/usr/bin/env python3

import sys
import bisect

def update(lst, p):
    keys = [i for c, i in lst]
    keys.reverse()
    pos = len(lst) - bisect.bisect(keys, p[1])
    lst[pos:pos] = [p]

def solve(ps):
    lst = [[chr(ord('A')+i), p] for i,p in enumerate(ps)]
    lst.sort(key=lambda x:x[1], reverse=True)
    ret = []
    while len(lst)>0:
        if lst[0][1] == 1 and len(lst) >= 3:
                ret.append(lst[0][0])
                lst = lst[1:]
        elif lst[0][1] == lst[1][1]:
            ret.append(lst[0][0] + lst[1][0])
            if lst[0][1] == 1:
                lst = lst[2:]
            else:
                lst[0][1] -= 1
                lst[1][1] -= 1
                p1 = lst[0]
                p2 = lst[1]
                lst = lst[2:]
                update(lst, p1)
                update(lst, p2)
        elif lst[0][1] == lst[1][1] + 1:
            ret.append(lst[0][0])
            lst[0][1] -= 1
        else:
            ret.append(lst[0][0]*2)
            lst[0][1] -= 2

    return ret

def main():
    t = int(sys.stdin.readline())
    for i in range(0,t):
        sys.stdin.readline()
        ps = [int(x) for x in sys.stdin.readline().split()]
        print("Case #{0}: {1}".format(i+1, ' '.join(solve(ps))))
if __name__ == '__main__':
    main()
