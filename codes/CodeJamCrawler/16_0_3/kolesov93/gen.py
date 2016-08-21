#!/usr/bin/env python
import random
n = 32
j = 500

powers = dict()
for d in xrange(2, 11):
    pws = []
    for i in xrange(n):
        pws.append(d ** i)
    powers[d] = pws


clim = 1000
checked = set()
while j > 0:
    q = [1] + [random.choice([0, 1]) for _ in xrange(n - 2)] + [1]
    strq = ''.join(str(x) for x in q)
    if strq in checked:
        continue
    checked.add(strq)

    cool = True
    divs = []
    for d in xrange(2, 11):
        m = 0
        for power, value in enumerate(q):
            m += value * powers[d][power]

        cool = False
        for i in xrange(2, clim):
            if m % i == 0:
                cool = True
                divs.append(i)
                break

        if not cool:
            break

    if cool:
        j -= 1
        print strq[::-1], ' '.join(str(x) for x in divs)


