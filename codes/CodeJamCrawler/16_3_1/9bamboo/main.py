#!/usr/bin/python3
# -*- coding: utf-8 -*-
# †
lmap = lambda func, *it: list(map(func, *it))
lfilter = lambda func, *it: list(filter(func, *it))
from functools import reduce
lreduce = lambda func, *it: list(reduce(func, *it))

from string import ascii_uppercase as upper
from collections import namedtuple
from itertools import chain, repeat

def Struct(name, fields):
    fields = fields.replace(',', ' ').split()
    def __init__(self, *args):
        n, m = len(args), len(fields)
        if n > m:
            raise TypeError('__init__() takes at most {} arguments ({} given)'.format(m, n))
        args = chain(args, repeat(None))
        for field, value in zip(fields, args):
            setattr(self, field, value)
    def __str__(self):
        return '{}({})'.format(name, ', '.join('{}={}'.format(f, getattr(self, f)) for f in fields))
    def __getitem__(self, index):
        return getattr(self, fields[index])
    def __setitem__(self, index, value):
        setattr(self, fields[index], value)
    attrs = {
        '__slots__': fields,
        '__init__':  __init__,
        '__getitem__': __getitem__,
        '__setitem__': __setitem__,
        '__str__':  __str__,
        '__repr__': __str__,
    }
    return type(name, (object,), attrs)

T = Struct('T', 'index, val')

from itertools import zip_longest
# grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

t = int(input())
for loop in range(t):
    n = int(input())
    p = list(T(*pr) for pr in enumerate(map(int, input().split())))
    arr = []
    while any(pr.val > 0 for pr in p):
        p.sort(key=lambda x: (-x.val, x.index))
        if p[0].val > 0:
            tmp = upper[p[0].index]
            p[0].val -= 1
        arr.append(tmp)
    grp = list(grouper(arr, 2, ''))
    last = ''.join(grp[-1])
    if len(last) == 1:
        assert len(grp[-2]) == 2
        last3 = ''.join(''.join(g) for g in grp[-2:])
        res = ' '.join(''.join(g) for g in grp[:-2])
        ext = ' '.join([last3[:1], last3[1:]])
        res += ' ' + ext
    else:
        res = ' '.join(''.join(g) for g in grp)
    print('Case #{}: {}'.format(loop+1, res))
