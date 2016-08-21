n = int(raw_input())

for i in range(n):
    start = int(raw_input())
    seen_digits = set([])

    if start == 0:
        print "Case #%d: INSOMNIA" % (i+1)
        continue

    k = 1
    next = k * start
    done = False
    while True:
        next = k * start

        for c in str(next):
            seen_digits.add(c)
            if len(seen_digits) == 10:
                done = True
                break

        if done:
            break

        k += 1

    print "Case #%d: %d" % (i+1, next)
