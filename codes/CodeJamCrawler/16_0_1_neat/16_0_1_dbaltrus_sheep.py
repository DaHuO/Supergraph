from sys import stdin

lines = stdin.readlines()
t = 0
for line in lines[1:]:
    t += 1
    start = int(line)
    if start == 0:
        print "Case #%d: INSOMNIA" % t
        continue
    number = start
    seen = set(str(number))
    while len(seen) < 10:
        number += start
        seen |= set(str(number))
    print "Case #%d: %d" % (t, number)