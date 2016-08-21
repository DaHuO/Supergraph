import fileinput

for t, l in enumerate(fileinput.input()):
    if t == 0: continue
    pm = l.strip()
    flips = 0
    for i in range(1, len(pm)):
        if (pm[i] != pm[i - 1]):
            flips += 1
    if pm[-1] == '-':
        flips += 1
    print "Case #%i: %i" % (t, flips)
