# -*- coding: utf-8 -*-
"""
Created on Sun May 08 15:23:20 2016

@author: abhibhat
"""
def CJ1C2016PB1(sen):
    from collections import Counter
    from string import ascii_uppercase
    sen = Counter(dict(zip(ascii_uppercase, sen)))
    last,  out = [], []
    for _ in range(sum(sen.values())):
        mc = sen.most_common(1)[0][0]
        out.append(mc)
        sen[mc] -= 1
    if len(out) % 2 and len(out) > 1:
        last = out[-2:]
        out = out[:-2]
    for i in range(0, len(out), 2):
        yield ''.join(out[i: i + 2])
    yield ''.join(last)
N = input()
for t in range(1, N+1):
    _ = input()
    print 'Case #{}: {}'.format(t, ' '.join(CJ1C2016PB1(map(int, raw_input().split()))))
    