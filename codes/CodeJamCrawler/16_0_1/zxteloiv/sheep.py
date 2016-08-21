# coding: utf-8

import  sys

def output(i, result):
    print "Case #%d: %s" % (i, str(result))

def small_dataset(i, num):
    seen_digits = set()

    loop = 0
    base = num
    while len(seen_digits) < 10:
        loop += 1
        num = base * loop

        numstr = str(num)
        seen_digits = seen_digits.union(set(numstr))

    output(i, num)

def process(i, num):
    if num == 0:
        output(i, "INSOMNIA")
        return

    small_dataset(i, num)
    return

    if num == 1:
        output(i, 10)

    if num == 2:
        output(i, 90)

    if num == 11:
        output(i, 110)

    if num == 1692:
        output(i, 5076)
    
    pass

T = int(raw_input())
for i in xrange(T):
    process(i + 1, int(raw_input()))

