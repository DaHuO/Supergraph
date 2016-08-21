#!/usr/bin/python

import sys

f = open(sys.argv[1])
o = open(sys.argv[2], 'w')
cases = int(f.readline())
goal = set(range(10))
for i in xrange(cases):
    seen = set()
    n = int(f.readline())
    cur = 0
    while seen != goal and n != 0:
        cur += n
        digits = map(int, str(cur))
        seen = seen.union(set(digits))
    resul = "INSOMNIA" if n == 0 else str(cur)
    o.write("Case #" + str(i+1) + ': ' + resul + '\n')


o.close()
print "Done, output written"
 
