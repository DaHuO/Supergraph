# -*- coding: utf-8 -*-  
'''
Created on 16 Apr, 2016
'''

DATA_FILE_NAME = 'A-small-attempt0.in'
DATA_FILE_NAME = 'A-large.in'
# DATA_FILE_NAME = 'B-large-practice.in'
# DATA_FILE_NAME = 'test_data_b.dat'
# DATA_FILE_NAME = 'A_test.in'
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
                    #line_no = int(line_iter.next().split()[1])
                    yield idx + 1, [line_iter.next().strip() for _ in range(line_no+1)]
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
    #import bisect
    from collections import Counter

    S = case_data[0]
    c = Counter(S)

    num = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    Counter("".join(["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]))
    cha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    import numpy as np
    colnum = 10
    rownum = len(cha)
    rst = Counter()

    rst[0] = c['Z']
    rst[6] = c['X']
    rst[8] = c['G']
    rst[3] = c['H'] - rst[8]
    rst[4] = c['U']
    rst[2] = c['W']
    rst[1] = c['O'] - rst[0] - rst[2] - rst[4]
    rst[7] = c['S'] - rst[6]
    rst[5] = c['V'] - rst[7]
    rst[9] = c['I'] - rst[5] - rst[6] - rst[8]
    Counter({'E': 9,
             'F': 2,                    # 4 5
             'G': 1,            # 8
             'H': 2,                    # 3 8
             'I': 4,                            # 5 6 8 9
             'N': 4,                            # 1 7 99
             'O': 4,                            # 0 1 2 4
             'R': 3,                            # 0 3 4
             'S': 2,                    # 6 7
             'T': 3,                            # 2 3 8
             'U': 1,            # 4
             'V': 2,                    # 5 7
             'W': 1,            # 2
             'X': 1,            # 6
             'Z': 1     }        )  # 0

    rr = ''
    for i in range(10):
        if rst[i]>0:
            rr += str(i)*rst[i]


    return rr


for idx, case_data in data_iterator(lines_to_read=1):
    case_out = solve(case_data)
    #print case_data
    # print '========================'
    result_tmp = 'Case #%d: %s\n' % (idx, case_out)
    #print case_out
    result_out += result_tmp
# print result_out

if not SHELL_PIPE_FLAG:
    import os

    if not os.path.exists('Out'):
        os.makedirs('Out')

    with open('./Out/' + DATA_FILE_NAME + '.out', 'wb') as f:
        f.write(result_out)

#with open(DATA_FILE_NAME+'.out','wb') as f:
#    f.write(result_out)
