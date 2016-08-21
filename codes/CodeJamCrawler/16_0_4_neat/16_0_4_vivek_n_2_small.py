#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

for tc in range(input()):
    k,c,s=map(int,raw_input().split())
    print 'Case #%d:'%(tc+1),
    for i in range(k):
        print i+1,
    print
