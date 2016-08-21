def extract(y):
    return set([int(j) for j in str(y)])

T = input()

for i in range(T):
    N = input()

    if N == 0:
        last = "INSOMNIA"
    else:
        last = N
        digits = extract(N)

        while (digits != set(range(10))):
            last += N
            digits = digits.union(extract(last))

    print "Case #%d: %s" % (i + 1, last)