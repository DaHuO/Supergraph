#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cases = int(input().strip())

for i, x in enumerate(range(cases), 1):
    pancake_seq = input().strip()
    first = pancake_seq[0:1]  # First in list
    temp = first
    positive = True if first == '+' else False

    flips = 0
    for sign in pancake_seq:
        if sign != temp:
            flips += 1
            positive = not positive
        temp = sign

    if not positive:
        flips += 1

    print("Case #{0:s}:".format(str(i)), str(flips))
