#!/usr/bin/env python2.7
import sys
lines = iter(sys.stdin)
cases = int(lines.next())
def get_max_keys(D):
    assert len(D) > 0
    curr_max = -1
    curr_keys = []
    for key, val in D.iteritems():
        if val > curr_max:
            curr_keys = [key]
            curr_max = val
        elif val == curr_max:
            curr_keys.append(key)
    return curr_keys
for case in range(1,cases+1):
    out = []
    N = lines.next()
    nums = map(int, lines.next().split())
    total = sum(nums)
    current = {chr(ord('A') + i): val for i, val in enumerate(nums)}
    while total > 0:
        keys = get_max_keys(current)
        if len(keys) in [1,3]:
            key = keys[0]
            out += key
            current[key] -= 1
            total -=1
        else:
            out.append(''.join([keys[0], keys[1]]))
            current[keys[0]] -= 1
            current[keys[1]] -= 1
            total -= 2
    out = ' '.join(out)
    print "Case #{case}: {out}".format(case=case, out=out.strip())
