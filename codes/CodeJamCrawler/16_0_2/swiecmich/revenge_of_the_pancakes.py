import itertools


t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    s_grouped = list(group[0] for group in itertools.groupby(s))
    res = len(s_grouped)
    while res > 0 and s_grouped[res - 1] == '+':
        res -= 1
    print "Case #{}: {}".format(i, res)
