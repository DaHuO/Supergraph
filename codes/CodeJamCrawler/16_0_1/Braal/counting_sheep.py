
t = int(raw_input())
sheep = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

for i in xrange(1, t+1):
    N = int(raw_input())

    if N == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
        continue

    seen = set()
    for x in xrange(1, 1000000):
        seen |= set(str(x * N))

        if not (sheep - seen):
            print "Case #{}: {}".format(i, x*N)
            break
    else:
        print "Case #{}: {}".format(i, "INSOMNIA")
