"""
@author     :   Rajan Khullar
@created    :   04/08/16
"""


def alg(N):
    if N == 0:
        return 'INSOMNIA'

    bloom = []  # counting bloom filter indexed 0 to 9
    for i in range(10):
        bloom.append(0)

    c = 1
    n = N
    while True:
        # update bloom filter with current N
        t = n
        while t > 0:
            bloom[t % 10] += 1
            t /= 10

        # check if every index of bloom is not zero
        test = True
        for i in range(10):
            if bloom[i] == 0:
                test = False
        if test:
            break

        c += 1
        n = c * N

    return n

if __name__ == '__main__':
    from sys import argv

    if len(argv) < 2:
        exit(1)

    INPUT = argv[1]

    i = 1
    with open(INPUT, 'r') as file:
        next(file)
        for line in file:
            t = int(line)
            o = alg(t)
            print "Case #{:d}: {:s}".format(i, str(o))
            i += 1
