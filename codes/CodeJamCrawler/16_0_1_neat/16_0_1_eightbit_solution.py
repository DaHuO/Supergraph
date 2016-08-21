def solve(N):
    if N == 0:
        return "INSOMNIA"

    solution = N
    digits = []
    multiplier = 2
    while len(digits) < 10:
        while solution > 0:
            if not (solution % 10) in digits:
                digits.append(solution % 10)
            solution /= 10
        solution = multiplier * N
        multiplier += 1
    return N * (multiplier - 2)

if __name__ == '__main__':
    lines = open('A-large.in', 'r').readlines()
    test_cases = int(lines[0])
    for i in xrange(1, len(lines)):
        N = int(lines[i])

        print 'Case #{0}: {1}'.format(i, solve(N))