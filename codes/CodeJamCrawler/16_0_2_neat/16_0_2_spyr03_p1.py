n = int(raw_input())

for test in xrange(n):
    line = raw_input()
    line += "+"
    count = 0
    size = len(line)
    for i in range(1, size):
        if line[i] != line[i-1]:
            count += 1
    print "Case #{}: {}".format(test+1, count)