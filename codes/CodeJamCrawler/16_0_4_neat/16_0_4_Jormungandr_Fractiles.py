#!/usr/bin/env python

__author__ = 'Bill'

from misc import input_, output_

num_cases, cases = input_('D-small-attempt0.in')

results = []

for case in cases:
    case = case.rstrip('\n')
    K = int(case.split(' ')[0])
    C = int(case.split(' ')[1])
    S = int(case.split(' ')[2])
    Kc = K**C
    if Kc == 1:
        results.append('1')
        continue
    elif C == 1 and K == S:
        tmp_str = ""
        for i in xrange(K):
            tmp_str += str(i+1) + ' '
        results.append(tmp_str.rstrip(' '))
        continue
    num_blocks = Kc/K
    middle = num_blocks%2
    if middle%2 == 0:
        tmp_str = ""
        mid = (num_blocks/2 - 1)*K + 1 + K/2
        for i in xrange(K):
            tmp_str += str(mid + i) + ' '
        results.append(tmp_str.rstrip(' '))
    else:
        tmp_str = ""
        mid = num_blocks/2
        origin_block_start = K*mid
        for i in xrange(K):
            tmp_str += str(origin_block_start + i +1) + ' '
        results.append(tmp_str.rstrip(' '))

output_(results, 'Fractiles_small.out')
