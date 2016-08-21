# Bloody Commas
def sc(txt):
    z = "+"
    k = 0
    for v in txt[::-1]:
        if v != z:
            k += 1
            z = v
    return k

from sys import stdin

for i in xrange(int(stdin.readline())):
    print "Case #%d: %d" % (i + 1, sc(stdin.readline().strip()))
