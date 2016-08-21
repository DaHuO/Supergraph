#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
def get_first_different_side(top, pancake):
    pos = 1
    while (pos < len(pancake) and pancake[pos] == top):
        pos += 1
    return pos if pos < len(pancake) else -1

def flip_pancake(pancake):
    top = pancake[0]
    split_position = get_first_different_side(top, pancake)
    if split_position == -1:
        return 0 if top == '+' else 1
    return flip_pancake(pancake[split_position:]) + 1

T = int(input())

for case in range(T):
    pancake = input()
    print("Case #{0}: {1}".format(case + 1, flip_pancake(pancake)))

