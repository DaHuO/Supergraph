import sys
import utils

fname = sys.argv[1]

def get_ans(case):
    K, C, S = case[0]

    tiles_to_check = []

    prev_skip = K ** (C-1)
    if C == 1:
        prev_skip = 0

    for i in range(K):
        tiles_to_check.append(i * prev_skip + i)

    return ' '.join([str(x + 1) for x in tiles_to_check])

utils.process(fname, 1, [lambda x: [int(y) for y in x.strip().split()]], get_ans)
