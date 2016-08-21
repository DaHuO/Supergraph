#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())

for case_id in xrange(1, N + 1):
    num = int(sys.stdin.readline())
    if num == 0:
        print "Case #%d: INSOMNIA" % case_id
        continue
    digits, total, current_num = [0] * 10, 0, num
    while total < 10:
        next_num = current_num + num
        while current_num != 0:
            digit = current_num % 10
            current_num /= 10
            if digits[digit] == 0:
                digits[digit] = 1
                total += 1
        current_num = next_num
    print "Case #%d: %d" % (case_id, current_num - num)
