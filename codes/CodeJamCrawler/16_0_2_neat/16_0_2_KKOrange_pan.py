#!/usr/bin/python

import sys

l = map(str.strip, sys.stdin.readlines())

idx = 0
for i in l[1:]:
    idx += 1
    cur = '?'
    ans = 0
    if i.count('-') == len(i):
        ans = 1
    elif i.count('+') == len(i):
        ans = 0
    else:
#        print i
        for c in i:
#            print "Looking at ", c
            if c == cur or cur == '?':
#                print "matches"
                if c == '-':
                    cur = '+'
                else:
                    cur = '-'
                ans += 1
#        print "Last character was ", i[-1]
        if i[-1] == '+':
            ans -= 1
    print "Case #%d: %d" % (idx, ans)


