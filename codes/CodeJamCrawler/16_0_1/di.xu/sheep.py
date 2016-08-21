

import sys
f = sys.stdin
cases = int(f.readline())
for case in range(1,cases+1):
    n = int(f.readline())
    seen = set()
    if n != 0:
        i = 1
        while n/i > 0:
            i *= 10
            upper = i*i
        cur = n
        while cur <= upper:
            seen.update(set(str(cur)))
            if len(seen) == 10:
                print "Case #%d: %d" % (case,cur)
                break
            cur += n
    if len(seen) < 10:
        print "Case #%d: INSOMNIA" % (case)
