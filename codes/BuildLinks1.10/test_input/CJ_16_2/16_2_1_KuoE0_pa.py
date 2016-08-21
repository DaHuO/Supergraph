#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

word_of_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def try_digit(word_str):
    if word_str == '':
        return (True, '')

    for idx,d in enumerate(word_of_number):
        char_set = set(d)
        if all([d.count(c) <= word_str.count(c) for c in char_set]):
            remain = word_str
            for c in char_set:
                remain = remain.replace(''.join([c] * d.count(c)), '', 1)
            ret = try_digit(remain)
            if ret[0]:
                return (True, ret[1] + str(idx))
    return (False, '')

T = int(input())
for t in range(T):
    S = ''.join(sorted(input().lower()))
    ret = try_digit(S)
    ret = ''.join(sorted(ret[1]))
    print("Case #{0}: {1}".format(t + 1, ret))


