import itertools

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    # consolidate pancakes
    cakeParts = [''.join(part) for key, part in itertools.groupby(s)]
    # remove trailing pancakes
    if '+' in cakeParts[-1]:
        cakeParts.pop()
    print "Case #{}: {}".format(i, len(cakeParts))
        
