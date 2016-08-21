#!/usr/bin/env python


def countsheep(num):

    if int(num) == 0:
        return "INSOMNIA"

    mult = 1
    seen = set()
    last_seen = num
    for ch in (str(num)):
        seen.add(int(ch))

    while len(seen) != 10:
        result = num * mult
        mult += 1
        for ch in (str(result)):
            seen.add(int(ch))
        last_seen = result
    return last_seen


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, countsheep(n))
