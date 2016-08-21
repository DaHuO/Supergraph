# -*- coding: utf-8 -*-  
'''
Created on 16 Apr, 2016
https://code.google.com/codejam/contest/2270488/dashboard#s=a&a=0
'''

DATA_FILE_NAME = 'B-small-attempt2.in'
DATA_FILE_NAME = 'B-large.in'
# DATA_FILE_NAME = 'B-large-practice.in'
# DATA_FILE_NAME = 'test_data_b.dat'
# DATA_FILE_NAME = 'B_test.in'
SHELL_PIPE_FLAG = False


# =================================================================


def data_iterator(lines_to_read=None):
    if not SHELL_PIPE_FLAG:
        with open(DATA_FILE_NAME, 'r') as f_handle:
            line_iter = f_handle.xreadlines()
            case_no = int(line_iter.next())
            for idx in range(case_no):
                if not lines_to_read:
                    line_no = int(line_iter.next())
                    # line_no = int(line_iter.next().split()[1])
                    yield idx + 1, [line_iter.next().strip() for _ in range(line_no*2 - 1)]
                else:
                    yield idx + 1, [line_iter.next().strip() for _ in range(lines_to_read)]
    else:
        import sys  # raw_input() sys.stdin.readline()
        case_no = int(sys.stdin.readline())
        for idx in range(case_no):
            if not lines_to_read:
                line_no = int(sys.stdin.readline())
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(line_no)]
            else:
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(lines_to_read)]


result_out = ''

import numpy as np
import scipy.misc as sc_m

def c_b(B):
    # 2**(B-2)
    s = 0
    for i in range(B-1):
        s += sc_m.comb(B-2, i, exact=True)
    return s

def solve(case_data):
    B,M = map(int,case_data[0].split(' '))

    max_m = c_b(B)
    if M > c_b(B):
        return 'IMPOSSIBLE'

    diff =  max_m - M
    if diff == 0:
        b ='0' +'1'*(B-2)
    else:
        b = bin(diff)[2:]
        b = b.replace('0','a').replace('1', '0').replace('a', '1')
        b = '0'+ '1'*(B-len(b)-2) + b



    rst = []
    rst.append(b + '1')

    for i in range(1,B):
        rst.append('0'*(i+1) + '1'*(B-i-1))

    return 'POSSIBLE\n' +    '\n'.join(rst)


for idx, case_data in data_iterator(lines_to_read=1):
    case_out = solve(case_data)
    # print case_data
    # print '========================'
    result_tmp = 'Case #%d: %s\n' % (idx, case_out)
    # print case_out
    result_out += result_tmp
# print result_out

if not SHELL_PIPE_FLAG:
    import os

    if not os.path.exists('Out'):
        os.makedirs('Out')

    with open('./Out/' + DATA_FILE_NAME + '.out', 'wb') as f:
        f.write(result_out)

# with open(DATA_FILE_NAME+'.out','wb') as f:
#    f.write(result_out)
