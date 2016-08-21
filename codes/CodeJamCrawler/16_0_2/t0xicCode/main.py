#!/usr/bin/env python

from __future__ import print_function

def output(s):
    c = 0

    while (s.count('+') < len(s)):
        while (s[-1] is '+'):
            s = s[:-1]

        i = 0
        if s[0] is '+':
            while (s[i] is '+'):
                i+=1
            
            s =''.join(['-' if x is '+' else '+' for x in reversed(s[:i])] + [x for x in s[i:]])
            c+=1

        s = ['-' if x is '+' else '+' for x in reversed(s)]
        c+=1

    return str(c)

num = int(raw_input())

for i in range(0, num):
    print(''.join(["Case #", str(i+1), ": ", output(raw_input())]))
