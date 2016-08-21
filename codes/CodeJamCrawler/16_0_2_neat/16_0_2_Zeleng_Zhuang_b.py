#!/usr/bin/env python
# coding=utf-8


def main2():
    s = raw_input()
    i = 0
    while True:
        l = len(s)
        if l == 0:
            break
        if s[l - 1] == '+':
            s = s[:-1]
        else:
            break
    if len(s) == 0:
        print 0
        return
    cnt = 0
    while i < len(s):
        cnt += 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            i += 1
        i += 1
    print cnt


for i in xrange(input()):
    print "Case #" + str(i + 1) + ":",
    main2()

