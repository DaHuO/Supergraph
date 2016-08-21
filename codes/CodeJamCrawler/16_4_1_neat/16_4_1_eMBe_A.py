# encoding: UTF-8

from __future__ import absolute_import, division

from future_builtins import *
range = xrange

import collections
import itertools
import sys

class gcj:
    IN = sys.stdin
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line_raw(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def _read_line_view(cls):
        line = cls._read_line_raw()
        if not isinstance(line, memoryview):
            line = memoryview(line)
        return line

    @classmethod
    def _read_line(cls):
        line = cls._read_line_raw()
        if isinstance(line, memoryview):
            line = line.tobytes()
        return line

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line_raw()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = memoryview(line)[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line_view()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i].tobytes())

    @classmethod
    def tokens(cls, cnt, conv=identity):
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return b'Case #{}:'.format(cls.current_case)

def result(a, b):
    results = {
        'PR': 'P',
        'RS': 'R',
        'PS': 'S',
    }
    if a < b:
        return results[a+b]
    else:
        return results[b+a]

memo = {}

def make(n, p, r, s, res):
    if max(p, r, s) - min(p, r, s) > 1:
        return None
    if p + r + s != 2**n:
        return None
    if (p, r, s, res) in memo:
        return memo[p, r, s, res]
    if n == 0:
        if p == res.count('P') and r == res.count('R') and s == res.count('S'):
            return res
        return None
    if res == 'P':
        sec = 'R'
    elif res == 'S':
        sec = 'P'
    elif res == 'R':
        sec = 'S'

    x = 2**(n-1) // 3
    for p1 in xrange(x, x+2):
        for r1 in xrange(x, x+2):
            for s1 in xrange(x, x+2):
                a = make(n-1, p1, r1, s1, res)
                if a is None:
                    continue
                b = make(n-1, p-p1, r-r1, s-s1, sec)
                if b is None:
                    continue
                q = min(a, b) + max(a, b)
                memo[p, r, s, res] = q
                return q
    return None

def solve():
    n, r, p, s = gcj.tokens(4, int)
    res = None
    for x in 'PRS':
        y = make(n, p, r, s, x)
        if y is not None:
            if res is None:
                res = y
            else:
                res = min(res, y)
    if res is not None:
        return res
    return 'IMPOSSIBLE'

def main():
    sys.setrecursionlimit(10000)
    t = gcj.token(int)
    for _ in xrange(t):
        print gcj.case(), solve()
        sys.stdout.flush()

main()
