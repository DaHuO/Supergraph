import os
import sys
import fileinput

for line in fileinput.input():
    i = fileinput.lineno()
    if i == 1:
        continue

    base = n = int(line)

    if n == 0:
        print "Case #%i: INSOMNIA" % (i-1)
        continue

    seen = set(str(n))

    while len(seen) < 10:
        n += base
        seen = seen | set(str(n))


    print "Case #%i: %i" % (i-1, n)
