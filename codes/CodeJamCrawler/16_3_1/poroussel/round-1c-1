#!/usr/bin/env python

import fileinput

def fkey(el):
    return -el[1]

def resolve(npb, line):
    cnt = [int(c) for c in line.split(' ')]
    tpl = [('%c' % (65+idx), c) for idx, c in enumerate(cnt)]
    tpl = sorted(tpl, key=fkey)
    res = []
    while tpl != []:
        # print tpl
        if sum(el[1] for el in tpl) == 3 and len(tpl) > 2:
            tpl[0] = (tpl[0][0], tpl[0][1] - 1)
            res.append(tpl[0][0])
            if tpl[0][1] == 0:
                tpl.pop(0)
            tpl = sorted(tpl, key=fkey)
            continue

        if len(tpl) == 1:
            nb = min(2, tpl[0][1])
            tpl[0] = (tpl[0][0], tpl[0][1] - nb)
            res.append(tpl[0][0] * nb)
            if tpl[0][1] == 0:
                tpl.pop(0)
            tpl = sorted(tpl, key=fkey)
            continue

        mn = min(2, tpl[0][1] - tpl[1][1])
        if mn == 2:
            tpl[0] = (tpl[0][0], tpl[0][1] - 2)
            res.append(tpl[0][0] * 2)
            if tpl[0][1] == 0:
                tpl.pop(0)
        else:
            tpl[0] = (tpl[0][0], tpl[0][1] - 1)
            tpl[1] = (tpl[1][0], tpl[1][1] - 1)
            res.append(tpl[0][0]+tpl[1][0])
            if tpl[1][1] == 0:
                tpl.pop(1)
            if tpl[0][1] == 0:
                tpl.pop(0)
        tpl = sorted(tpl, key=fkey)

    return ' '.join(res)

if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        nbp = int(input.readline())
        print 'Case #{}: {}'.format(idx+1, resolve(nbp, input.readline()))
