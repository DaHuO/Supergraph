#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'huky'

import sys

digits = set()

def is_slept():
    for i in range(10):
        if i not in digits:
            return False
    return True

def get_digits(n):
    t = n
    d = set()
    while t > 0:
        d.add(t % 10)
        t /= 10
    return d

def main():
    global digits
    f = open('A-large.in', 'r')
    fo = open('A-large.out', 'w')
    case_num = int(f.readline().strip())
    for i in range(case_num):
        digits = set()
        fo.write("Case #%d: " % (i+1))
        x = int(f.readline().strip())
        print x
        if 0 == x:
            fo.write("INSOMNIA\n")
            continue
        digits = digits | get_digits(x)
        n = x
        while not is_slept():
            n += x
            digits = digits | get_digits(n)
        print digits, n
        print
        fo.write("%d\n" % n)
    f.close()
    fo.close()


if __name__ == "__main__":
    main()
