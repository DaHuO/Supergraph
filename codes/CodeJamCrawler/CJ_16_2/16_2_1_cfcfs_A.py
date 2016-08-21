#!/usr/bin/env python

import time
import sys
import random
sys.setrecursionlimit(10000)

def debug(*args, **kwargs):
    if args:
        sys.stderr.write('DEBUG: ' + (';'.join(['{0}'.format(str(v)) for v in args])) + '\n')
    if kwargs:
        sys.stderr.write('DEBUG: ' + (';'.join(['{0}:{1}'.format(k, str(v)) for k, v in kwargs.items()])) + '\n')
    pass

def count(c, s):
    return len(filter(lambda x: x == c, s))

start_time = time.time()
for case_num in xrange(1, int(raw_input()) + 1):
    debug('Processing Case #%d' % (case_num,))
    S = raw_input()
    debug(S=S)
    chars = {s: 0 for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for s in S:
        chars[s] = chars[s]+1
    #debug(chars=chars)
    res = ''
    for digit, word in [(0, 'ZERO'), (8, 'EIGHT'), (6, 'SIX'), (7, 'SEVEN'), (3, 'THREE'), (2, 'TWO'), (4, 'FOUR'), (5, 'FIVE'), (9, 'NINE'), (1, 'ONE')]:
        wc = {}
        for c in word:
            wc[c] = wc.get(c, 0)+1
        m = min([chars[c]/n for c, n in wc.items()])
        for c in wc.keys():
            chars[c] = chars[c] - m
        debug(word=word, m=m)
        res += str(digit) * m
    debug(chars=chars)
    res = ''.join(sorted(res))
    print "Case #{0}: {1}".format(case_num, res)

debug("--- %s seconds ---" % (time.time() - start_time))
