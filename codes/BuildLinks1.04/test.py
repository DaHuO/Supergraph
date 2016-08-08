#!/usr/bin/env python
# -*- coding: utf-8 -*-

from extractFunctions import extractFunctions

f = open('test_input/sort_codes/course_topsort.py', 'r')
funcs = extractFunctions(f)
print funcs