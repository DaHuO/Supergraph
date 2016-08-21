from collections import defaultdict


t = int(raw_input())
test_cases = defaultdict(set)

for x in xrange(1, t + 1):
    n = int(raw_input())
    if not n:
        print("Case #%d: INSOMNIA" % x)
        continue
    found = False
    output = "INSOMNIA"
    i = n
    while i <= 1000000 and not found:
        n_set = set([s for s in str(i)])
        test_cases[x] = test_cases[x].union(n_set)
        if len(test_cases[x]) == 10:
            found = True
        else:
            i += n
    if found:
        output = str(i)
    print("Case #%d: %s" % (x, output))
