import sys


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        pancakes = list(sys.stdin.readline().strip())
        pancakes = reversed(pancakes)
        flipped = False
        flips = 0

        for pancake in pancakes:
            if pancake == '-':
                if not flipped:
                    flips += 1
                    flipped = True
            else:
                if flipped:
                    flips += 1
                    flipped = False

        print 'Case #{0}: {1}'.format(case+1, flips)


if __name__ == '__main__':
    main()
