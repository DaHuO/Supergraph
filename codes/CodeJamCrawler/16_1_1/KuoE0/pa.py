#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys

T = int(input())

for case in range(T):
    s = input()
    ret = ''
    for c in s:
        ret = max(ret + c, c + ret)
    print("Case #{0}: {1}".format(case + 1, ret))
