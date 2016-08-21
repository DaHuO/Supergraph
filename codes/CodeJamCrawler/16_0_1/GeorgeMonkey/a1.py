#!/bin/env python
from __future__ import print_function
import sys
import os
import os.path

fi = open(sys.argv[1], 'r')
fo = open(os.path.splitext(sys.argv[1])[0] + '.out', 'w')

T = int(fi.readline().strip())
for k in range(T):
    N = int(fi.readline().strip())
    if N == 0:
        ret = 'INSOMNIA'
    else:
        ret = 0
        dset = set(range(10))
        while len(dset) > 0:
            ret += N
            tval = ret
            if ret == 0:
                dset.discard(0)
            while tval != 0:
                dset.discard(tval % 10)
                tval = int(tval / 10)
    print('Case #%d:' % (k + 1), ret, file=fo)

fi.close()
fo.close()
