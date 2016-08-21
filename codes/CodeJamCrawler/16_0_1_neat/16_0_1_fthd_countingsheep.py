t = int(raw_input())  # read a line with a single integer

def ans(n):
    found = {}

    if n == 0:
        return "INSOMNIA"

    i = 1
    while len(found) < 10:
        curr = i*n
        for j in list(str(curr)):
            found[j] = 1

        i += 1

    return curr

for i in xrange(1, t + 1):
    n = int(raw_input())

    res = ans(n)

    print "Case #{}: {}".format(i, res)
