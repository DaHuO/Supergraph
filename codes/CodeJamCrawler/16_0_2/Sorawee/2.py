import sys
from itertools import *
for i, v in enumerate(sys.stdin.read().split()[1:]):
    print('Case #{}: {}'.format(
        i + 1,
        len(list(groupby(dropwhile(lambda x: x == '+', reversed(v)))))))