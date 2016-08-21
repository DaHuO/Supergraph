num_test_cases = int(raw_input().strip(" "))


def min_flips(order):
    pre = 'n'
    flips = 0
    for c in order:
        if pre == 'n':
            pre = c
            continue
        if c != pre:
            pre = c
            flips += 1

    if pre == '-':
        flips += 1
    return flips


for case in xrange(1, num_test_cases + 1):
    print "Case #%d: %d" % (case, min_flips(raw_input().strip(" ")))
