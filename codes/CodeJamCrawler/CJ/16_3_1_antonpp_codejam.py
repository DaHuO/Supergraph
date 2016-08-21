from collections import Counter
from collections import defaultdict
import itertools
import sys
import string
import re

sys.setrecursionlimit(100000)



with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    tt = int(next(input))
    for test in range(tt):
        print (test)
        n = int(next(input))
        p = [int(x) for x in next(input).split()]
        ans = []
        while max(p) > 0:
            m = max(p)
            mi = [i for i, j in enumerate(p) if j == m]
            if len(mi) == 1:
                p[mi[0]] -= 1
                ans.append(string.ascii_uppercase[mi[0]])
            else:
                if (len(filter(lambda x: x > 0, p)) == 2):
                    p[mi[0]] -= 1
                    p[mi[1]] -= 1
                    ans.append(string.ascii_uppercase[mi[0]] + string.ascii_uppercase[mi[1]])
                else:
                    p[mi[0]] -= 1
                    ans.append(string.ascii_uppercase[mi[0]])


        output.write('Case #{}: {}\n'.format(test + 1, ' '.join(ans)))
