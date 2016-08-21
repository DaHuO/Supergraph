#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

num = '7 3 9 0 1 2 4 5 6 8'.split()
words = 'seven three nine zero one two four five six  eight '.split()
my_dict = dict(zip(words, num))


def get_num(inp):
    """
    :type inp: string
    """

    inp = inp.lower()
    res=[]
    tmp = list(inp)

    x = tmp.count('x')
    for i in range(x):
        for c in 'six':
            tmp.remove(c)

    s = tmp.count('s')
    for i in range(s):
        for c in 'seven':
            tmp.remove(c)

    g = tmp.count('g')
    for i in range(g):
        for c in 'eight':
            tmp.remove(c)

    z = tmp.count('z')
    for i in range(z):
        for c in 'zero':
            tmp.remove(c)

    w = tmp.count('w')
    for i in range(w):
        for c in 'two':
            tmp.remove(c)

    u = tmp.count('u')
    for i in range(u):
        for c in 'four':
            tmp.remove(c)

    t = tmp.count('t')
    for i in range(t):
        for c in 'three':
            tmp.remove(c)

    v = tmp.count('v')
    for i in range(v):
        for c in 'five':
            tmp.remove(c)

    o = tmp.count('o')
    for i in range(o):
        for c in 'one':
            tmp.remove(c)

    i = tmp.count('i')
    for j in range(i):
        for c in 'nine':
            tmp.remove(c)

    res = '0'*z+'1'*o+'2'*w+'3'*t+'4'*u+'5'*v+'6'*x+'7'*s +'8'*g+'9'*i

    return res


T = int(raw_input())

for case in range(1, T + 1):
    S = raw_input()
    out = get_num(S)
    print 'Case #%d: %s' % (case, out)