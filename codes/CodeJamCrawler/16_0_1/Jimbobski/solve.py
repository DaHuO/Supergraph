
import sys

import numpy as np

f = open(sys.argv[1], 'rt')
lines = f.readlines()
f.close()

numbers = [int(l.strip()) for l in lines]

for case_i, num in enumerate(numbers[1:]):
    if num == 0:
        i = -1
        seen = np.array([1]*10, dtype=bool)
    else:
        seen = np.array([0]*10, dtype=bool)
        i = 0

    while not np.all(seen):
        i += 1
        tmp = i * num
        idx = np.array([int(s) for s in str(tmp)])
        #print(tmp, idx)
        seen[idx] = 1
        if i > 1e9:
            i = -1
            break
    out_str = 'INSOMNIA' if i == -1 else str(tmp)
    print("Case #%i: %s" % (case_i+1, out_str))

