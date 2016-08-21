#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat May 28 23:43:03 2016 +0800
# $Author: jiakai <jia.kai66@gmail.com>

class Impossible(Exception):
    pass

def rsort(seq):
    if len(seq) == 1:
        return seq
    h = len(seq) // 2
    begin = rsort(seq[:h])
    end = rsort(seq[h:])
    if end < begin:
        begin, end = end, begin
    return begin + end

def prst(func):
    def wfunc(*args):
        rst = func(*args)
        print(args, rst)
        return rst
    return wfunc


#@prst
def solve(nP, nR, nS):
    if min(nP, nR, nS) < 0:
        raise Impossible()
    td = (nP + nR + nS) // 2
    if td == 0:
        ans = ''
        if nP: ans += 'P'
        if nR: ans += 'R'
        if nS: ans += 'S'
        return ans
    ans = []
    a, b, c = td - nS, td - nP, td - nR
    for i in solve(a, b, c):
        if i == 'P':
            o = 'R'
            a -= 1
        elif i == 'R':
            o = 'S'
            b -= 1
        else:
            o = 'P'
            c -= 1
        ans.append(i)
        ans.append(o)

    assert a == b == c == 0
    ans = rsort(ans)
    return ''.join(ans)


def main():
    nr_case = int(input())
    for i in range(nr_case):
        inp = list(map(int, input().split()))
        R, P ,S = inp[1:]
        try:
            ans = solve(P, R, S)
        except Impossible:
            ans = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i + 1, ans))

if __name__ == '__main__':
    main()



