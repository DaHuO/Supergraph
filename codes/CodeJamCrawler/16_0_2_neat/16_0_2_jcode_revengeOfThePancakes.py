__author__ = 'jcode'

import re

num_tests = int(raw_input())
for x in xrange(1, num_tests+1):
    s = raw_input()
    num_pat = len(re.findall(r"\+\-", s))
    moves = 0
    if s[0] == '+':
        moves = num_pat * 2
    else:
        moves = (num_pat * 2) + 1

    print "Case #{}: {}".format(x, moves)
