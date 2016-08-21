t = input()

for r in xrange(t):
    n = input()

    if n == 0:
        print "Case #" + str(r + 1) + ": INSOMNIA"
        continue

    seen = [0 for i in xrange(10)]

    def count(m):
        while m > 0:
            seen[m % 10] = 1
            m /= 10

    tot = n
    count(tot)
    while sum(seen) < 10:
        tot += n
        count(tot)

    print "Case #" + str(r + 1) + ": " + str(tot)