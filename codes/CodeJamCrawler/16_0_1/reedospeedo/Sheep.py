f = open('A-large.in', 'r')
t = int(f.readline())
output_file = open('A-large.out', 'w')
for i in xrange(1, t+1):
    allnum = 0
    d = 1
    num = []
    n = int(f.readline())
    if n == 0:
        output_file.write("Case #%d: INSOMNIA\n" % (i))
    else:
        while allnum < 1:
            x = d * n
            num += [int(z) for z in str(x)]

            if all(y in num for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
                output_file.write("Case #%d: %d\n" % (i, x))
                allnum += 1

            else:
                d += 1
output_file.close()
