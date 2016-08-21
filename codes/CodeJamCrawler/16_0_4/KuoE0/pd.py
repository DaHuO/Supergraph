#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

T = int(input())

for case in range(T):
    K, C, S = [int(x) for x in input().split()]
    answer = ' '.join([str(x) for x in range(K + 1)[1:]])
    print("Case #{0}: {1}".format(case + 1, answer))

