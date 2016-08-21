#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def main():
    t = int(input())
    for tc in range(t):
        n = int(input())
        p = list(map(int, input().split(' ')))
        psum = sum(p)
        out = list()

        for tw in range(int(psum / 2)):
            bi = 0
            for i, x in enumerate(p):
                if x > p[bi]:
                    bi = i
            nbi = 0 if bi != 0 else 1
            for i, x in enumerate(p):
                if i == bi:
                    continue
                if x > p[nbi]:
                    nbi = i

            p[bi] -= 1
            p[nbi] -= 1
            s = chr(65 + bi) + chr(65 + nbi)
            out.insert(0, s)

        # handle last odd one
        s = ''
        if psum % 2 == 1:
            # do last one
            mi = p.index(max(p))
            s += chr(65 + mi)
            out.insert(0, s)

        toutput = 'Case #%d: ' % (tc + 1)
        for sen in out:
            toutput += sen + ' '
        toutput = toutput.strip()
        print(toutput)

if __name__ == '__main__':
    main()
