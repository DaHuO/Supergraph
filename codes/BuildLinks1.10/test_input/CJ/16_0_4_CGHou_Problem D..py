# -*- coding: utf-8 -*-  
'''
Created on 9 Apr, 2016
https://code.google.com/codejam/contest/2270488/dashboard#s=a&a=0
@author: a0086303
'''

DATA_FILE_NAME = 'D-small-attempt0.in'
DATA_FILE_NAME = 'D-large.in'
# DATA_FILE_NAME = 'B-large-practice.in'
# DATA_FILE_NAME = 'test_data_b.dat'
# DATA_FILE_NAME = 'D_test.in'
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
                    yield idx + 1, [line_iter.next().strip() for _ in range(line_no + 1)]
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


def solve(case_data):
    # from sympy.functions.combinatorial.numbers import nC, nP, nT
    # import bisect
    # from collections import Counter

    # N,X,K,A,B,C = map(int,case_data[0].split())
    K, C,  S = map(int,case_data[0].split())
    if K ==1:
        if S >0:
            return '1'
        else:
            return 'IMPOSSIBLE'

    c_part_liSt = []
    start_L = 0
    while start_L < K:
        if start_L + C <= K:
            c_part_liSt.append(range(start_L,start_L+C))
        else:
            tmp = range(start_L,K)
            tmp.extend([K-1]* (start_L + C - K))
            c_part_liSt.append(tmp)
            break
        start_L += C
    if S < len(c_part_liSt):
        return 'IMPOSSIBLE'

    rst = []
    for seq in c_part_liSt:
        pos = 1
        for idx, num in enumerate(seq):
            pos += num * K ** (C - idx - 1)
        rst.append(str(pos))

    return ' '.join(rst)


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
