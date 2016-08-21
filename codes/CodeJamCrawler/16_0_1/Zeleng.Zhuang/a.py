#!/usr/bin/env python
# coding=utf-8
import math

def main2():
    D = input()
    if D == 0:
        print "INSOMNIA"
        return
    st = set()
    x = D
    for _ in xrange(30000000):
        cur = D
        while cur > 0:
            st.add(cur % 10)
            cur /= 10
        if len(st) == 10:
            print D
            return
        D += x

for i in xrange(input()):
    print "Case #" + str(i + 1) + ": ",
    main2()

