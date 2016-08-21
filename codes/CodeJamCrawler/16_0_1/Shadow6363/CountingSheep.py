import sys


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        N = int(sys.stdin.readline().strip())

        if N == 0:
            number = 'INSOMNIA'
        else:
            named = set(str(N))
            multiplier = 1

            while len(named) < 10:
                multiplier += 1
                named |= set(str(multiplier*N))

            number = multiplier*N

        print 'Case #{0}: {1}'.format(case+1, number)


if __name__ == '__main__':
    main()
