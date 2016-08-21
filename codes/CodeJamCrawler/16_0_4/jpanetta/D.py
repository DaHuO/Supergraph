import fileinput

# Dumb small solution
for t, l in enumerate(fileinput.input()):
    if t == 0: continue
    K, C, S = map(int, l.strip().split())
    print "Case #%i: %s" % (t, " ".join(map(str, [K**(C - 1) * i + 1 for i in range(K)])))
