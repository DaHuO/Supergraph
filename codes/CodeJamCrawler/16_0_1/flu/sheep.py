#!/usr/bin/env python

def task(num):
    if num == 0:
        return 'INSOMNIA'
    seen = set()
    working_num = 0
    while len(seen) < 10:
        working_num += num
        for s in str(working_num):
            seen.add(s)
    return working_num

if __name__ == '__main__':
    T = int(input())
    i = 1
    while T > 0:
        res = task(int(input()))
        print("Case #{0}: {1}".format(i, res))
        i += 1
        T -= 1
