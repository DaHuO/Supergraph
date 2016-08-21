# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
import numpy as np
from collections import Counter
import string

def solve_case(num, cnts):
    counter = Counter()
    alph = list(string.ascii_uppercase)
    tot = 0
    ret = ""
    num_parties = num
    for i, cnt in enumerate(cnts.split(" ")):
        counter[alph[i]] = int(cnt)
        tot += int(cnt)
    
    while tot > 3:
        party, p_cnt = counter.most_common(2)[0]
        party2, p_cnt2 = counter.most_common(2)[1]
        if p_cnt > p_cnt2:
            ret += party+party + " "
            counter[party] -= 2
        else:
            ret += party + party2 + " "
            counter[party] -= 1
            counter[party2] -= 1
        tot -= 2
    
    if tot == 3:
        party, _ = counter.most_common(1)[0]
        ret += party + " "
        counter[party] -= 1
        tot -= 1
    if tot == 2:
        party, p_cnt = counter.most_common(2)[0]
        party2, p_cnt2 = counter.most_common(2)[1]
        ret += party + party2
        tot -= 2
    assert tot == 0
    return ret

num_cases = int(sys.stdin.readline())
for n in range(1, num_cases + 1):
    num_parties = int(sys.stdin.readline())
    counts = sys.stdin.readline()
    print("Case #{0}: {1}".format(n, solve_case(num_parties, counts)) )
