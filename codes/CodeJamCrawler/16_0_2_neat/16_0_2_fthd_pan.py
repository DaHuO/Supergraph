t = int(raw_input())  # read a line with a single integer

def ans(n):
    curr = 0

    if n[-1] == '-':
        curr += 1

    for i in xrange(1, len(n)):
        if n[i] != n[i-1]:
            curr += 1

    return curr

for i in xrange(1, t + 1):
    n = raw_input()

    res = ans(n)

    print "Case #{}: {}".format(i, res)
