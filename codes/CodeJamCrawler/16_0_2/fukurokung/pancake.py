#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Problem B: Revenge of the Pancakes
#Author: Wongnaret Khantuwan

def rotate(stack):
    result = ''
    for element in stack[::-1]:
        if element == '-':
            result+='+'
        else:
            result+='-'

    return result

def find_first_diff(stack):
    for i in range(0, len(stack)):
        if stack[i]!=stack[0]:
            return i

    return -1


def test(stack):
    loop = 0

    while stack.find('-') >= 0:
        if not '+' in stack:
            stack = rotate(stack)
        else:
            indx = find_first_diff(stack)
            stack = rotate(stack[:indx])+stack[indx:]
        loop+=1
    return loop

#main function
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  input = raw_input()
  print "Case #%d: %d" % (i, test(input))

