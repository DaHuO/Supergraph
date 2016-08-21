#!/usr/bin/env python
import itertools
import math
import sys

f = open('/dev/stdin', 'r')
T = int(f.readline())

def memoize(function, limit=None):
    if isinstance(function, int):
        def memoize_wrapper(f):
            return memoize(f, function)

        return memoize_wrapper

    dict = {}
    list = []
    def memoize_wrapper(*args, **kwargs):
        key = (args[0], args[1])
        try:
            list.append(list.pop(list.index(key)))
        except ValueError:
            dict[key] = function(*args, **kwargs)
            list.append(key)
            if limit is not None and len(list) > limit:
                del dict[list.pop(0)]

        return dict[key]

    memoize_wrapper._memoize_dict = dict
    memoize_wrapper._memoize_list = list
    memoize_wrapper._memoize_limit = limit
    memoize_wrapper._memoize_origfunc = function
    memoize_wrapper.func_name = function.func_name
    return memoize_wrapper

# @memoize(100000)
def factor(n, b):
    # sys.stderr.write(str(b) + '\n')
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return i

    return -1

for t in range(T):
    N, J = map(int, f.readline().strip().split())

    print('Case #%d:' % (t + 1))

    count = 0
    for j in map(''.join, itertools.product('01', repeat=N)):
        if j[0] != '1' or j[-1] != '1':
            continue
        # sys.stderr.write(j + '\n')

        factors = []
        for b in range(2, 10 + 1):
            n = int(j, b)
            f = factor(n, b)
            if f > 0:
                factors.append(f)
            else:
                break

        if len(factors) == 9:
            print(j + ' ' + ' '.join(map(str, factors)))
            count += 1

        if count >= J:
            break
