def sheep(case, n):
    if n == 0:
        print "Case #%d: INSOMNIA" % case
    else:
        z = set([str(x) for x in xrange(10)])
        x = set()
        i = 0
        while z - x != set():
            i += 1
            x = x.union(set(str(n * i)))
        print "Case #%d: %d" % (case, n * i)

if __name__ == '__main__':
    i = 1
    with open('A-large.in') as f:
        f.readline()
        for line in f:
            val = int(line.strip())
            sheep(i, val)
            i += 1