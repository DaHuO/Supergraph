# -*- encoding: utf-8 -*-
import re

def jian(s):
    # print('minus', s)
    if s.count("+") == len(s):
        return 1
    if s.count("-") == len(s):
        return 0

    ans = None
    for i in range(len(s)):
        t = ''.join(['+' if c == '-' else '-' for c in s[i::-1]]) + s[i+1:]
        # print('reversed', t, i)
        if t != s:
            if t.count("+") == len(s):
                return 2
            if t.count("-") == len(s):
                return 1
            if t[-1] == '+': # +++++
                cost = gao(re.match("[\-+]*-", t).group()) + 2
            else:  # -----
                cost = jian(re.match("[\-+]*\+", t).group()) + 1
        ans = min(ans, cost) if ans else cost

    return ans


def gao(s):
    # print('add', s)
    if s.count("+") == len(s):
        return 0
    if s.count("-") == len(s):
        return 1

    ans = None
    for i in range(len(s)):
        t = ''.join(['+' if c == '-' else '-' for c in s[i::-1]]) + s[i+1:]
        # print('reversed', t, i)
        if t != s:
            if t.count("+") == len(s):
                return 1
            if t.count("-") == len(s):
                return 2
            if t[-1] == '+':
                cost = gao(re.match("[\-+]*-", t).group()) + 1
            else:  # -
                cost = jian(re.match("[\-+]*\+", t).group()) + 2
        ans = min(ans, cost) if ans else cost

    return ans


n = int(input())
for i in range(n):
    s = input()
    print("Case #%s: %s" % (i+1, gao(s)))
