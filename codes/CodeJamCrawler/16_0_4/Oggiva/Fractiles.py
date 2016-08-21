from sys import stdin

t = int(stdin.readline())
for i in range(1, t+1):
    print "Case #%d:" % i,
    line = stdin.readline()
    splitted = line.split(" ")
    for k in xrange(1, int(splitted[0])+1):
        print k,
    print
