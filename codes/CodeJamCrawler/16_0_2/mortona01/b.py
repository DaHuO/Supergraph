#!/usr/bin/env python

import sys

stdin = sys.stdin
T = int(stdin.readline())

for i in range(1, T+1):
    S = list(stdin.readline().rstrip())

    stack_bottom = len(S) - 1
    stack_top = 0
    happy = False
    flips = 0
    while not happy:
        # print "S: {}".format(S)
        while S[stack_bottom] == '+' and stack_bottom >= stack_top:
            stack_bottom -= 1
            # print "bottom: {}".format(stack_bottom)

        if stack_bottom < stack_top:
            happy = True
            break

        section = list(S[stack_top:stack_bottom + 1])
        # print "section: {}".format(section)
        sect_size = len(section)

        
        # corner case where top and bottom of section have +,- respectively
        to_append = []
        if sect_size > 1 and section[0] == '+' and section[sect_size - 1] == '-':
            while section[stack_bottom] == '-' and stack_bottom >= stack_top:
                stack_bottom -= 1
                to_append.append(section[stack_bottom])
            size = sect_size - 1
            section = section[:stack_bottom + 1]
            stack_bottom = size
            # print "adjusted section: {}".format(section)
            # print "to append: {}".format(to_append)


        section = section[::-1]
        for j in range(0, len(section)):
            if section[j] == '+':
                section[j] = '-'
            else:
                section[j] = '+'
        flips += 1
        S = section + to_append

    print "Case #{}: {}".format(i, flips)
