def solve(n):
    i = 1
    seen = set()

    if n == 0:
        return 'INSOMNIA'

    while len(seen) < 10:
        digits = str(n * i)
        seen |= set(digits)
        i = i + 1

    return n * (i - 1)


if __name__ == '__main__':
    with open('input.txt') as f:
        cases = int(f.readline())
        for i in xrange(cases):
            print "Case #{i}: {solution}".format(
                i=i + 1, solution=solve(int(f.readline())))
