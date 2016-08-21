#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Problem A: Counting Sheep
#Author: Wongnaret Khantuwan

def split_digit(digit):
    return set(str(digit))

def test(digit):
    test_set = set()
    loop = 1

    if digit > 0:
        while len(test_set) < 10:
            tmp = digit * loop
            loop += 1
            test_set = test_set | split_digit(tmp)
        return tmp
    return 'INSOMNIA'

#main function
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  input = raw_input()
  print "Case #%d: %s" % (i, test(int(input)))

