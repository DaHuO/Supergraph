#!/usr/bin/env python

import sys
import os
import math
from collections import defaultdict, Counter

def get_answer(f):
    S = f.readline().strip()
    w = S[0]
    for i in xrange(1,len(S)):
        if S[i] >= w[0]:
            w = S[i] + w
        else:
            w = w + S[i]
    return w


if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = input_filename[:-3]+".out"
    if input_filename == "test":
        output_filename = "test.out"

    with open(input_filename) as f:
        with open(output_filename, "w") as g:
            T = int(f.readline().strip())
            for test_idx in xrange(1,T+1):
                ans = get_answer(f)
                g.write("Case #"+str(test_idx)+": "+str(ans)+"\n")

    #
