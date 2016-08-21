import itertools

for t in range(input()):
    print "Case #%s:" % str(t + 1),
    stack = raw_input().rstrip('+')
    print len(list(itertools.groupby( stack)))