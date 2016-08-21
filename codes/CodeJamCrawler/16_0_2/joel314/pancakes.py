#!/usr/bin/env python2.7
import sys
def get_negative(string):
    pos = string.rfind('+')
    if pos == -1:
        return 0
    else:
        return 1 + get_positive(string[:pos])
def get_positive(string):
    pos = string.rfind('-')
    if pos == -1:
        return 0
    else:
        return 1 + get_negative(string[:pos])
lines = iter(sys.stdin)
cases = int(lines.next())
for case in range(1,cases+1):
    S = lines.next()
    out = str(get_positive(S))
    print "Case #{case}: {out}".format(case=case, out=out.strip())
