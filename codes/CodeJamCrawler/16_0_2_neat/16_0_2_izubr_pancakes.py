def run(test):
    n_symbols = len(test)
    ideal = n_symbols * "+"
    if n_symbols == ideal:
        return 0
    state = test[0]
    flips = 0
    for cur in test[1:]:
        if cur != state:
            flips += 1
            state = cur
    if state == "-":
        flips += 1
    return flips

t = int(raw_input("").rstrip())
for i in range(t):
    print "Case #%s: %s" % (i + 1, run(raw_input("").rstrip()))
