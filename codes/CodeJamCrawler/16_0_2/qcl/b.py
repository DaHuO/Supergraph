# -*- coding: utf-8 -*-

import sys

def main():
    f = open(sys.argv[1])
    ncase = int(f.readline())
    for i in range(ncase):
        caseN = i + 1
        p = f.readline()[:-1]
        r = ''
        for gg in p:
            if len(r) == 0:
                r = r + gg
            elif not r[-1] == gg:
                r = r + gg
            else:
                pass
        times = len(r)
        if r[-1] == '+':
            times = times - 1
        print "Case #%d: %d" % (caseN, times)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
