#!/usr/bin/env python

__author__ = 'Bill'

from misc import input_, output_

num_cases, N_list, pages_list = input_('B-large.in')

Results = []

i = 0
for pages in pages_list:
    a = [item for page in pages for item in page]
    a.sort()
    c = [[x,a.count(x)] for x in set(a)]
    d = []
    for list in c:
        if (list[1]%2 != 0):
            d.append(list[0])
    d.sort()
    st = ''
    for item in d:
        st += str(item) + ' '
    Results.append(st.strip(' '))
    i += 1


output_(Results, 'B-large.out')