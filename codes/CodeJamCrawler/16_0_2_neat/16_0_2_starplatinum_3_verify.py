raw_input()

for i in xrange(50):
    ip = raw_input().split()
    jamcoin = ip[0]
    base_solutions = map(int, ip[1:])

    bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in xrange(len(bases)):
        if int(jamcoin, bases[i]) % base_solutions[i] != 0:
            print 'ALERT', jamcoin, bases[i], base_solutions[i]