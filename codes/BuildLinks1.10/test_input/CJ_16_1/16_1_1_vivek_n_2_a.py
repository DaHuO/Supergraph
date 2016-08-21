#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

for i in range(1,input()+1):
    x=raw_input()
    res=x[0]
    for j in x[1:]:
        if j>=res[0]:
            res=j+res
        else:
            res = res+j
    print "Case #%d:"%(i),res
