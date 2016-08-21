def solve_case(case):
    bottom = 0
    times = 0

    while bottom < len(case):
        while case[bottom] == '+':
            bottom += 1
            if bottom == len(case):
                return times
        assert case[bottom] == '-'

        top = len(case) - 1
        if case[top] == '+':
            while case[top] == '+':
                top -= 1
            for i in range(top+1, len(case)):
                case[i] = '-'
            times += 1
        case[bottom:] = reversed(case[bottom:])
        for i in range(bottom, len(case)):
            case[i] = '-' if case[i] == '+' else '+'
        times += 1

    return times


def main():
    INPUT_FILE = "B-large.in"
    with open(INPUT_FILE) as fh:
        cases = [l.rstrip() for l in fh.readlines()[1:]]

    sol = ''
    for i in range(len(cases)):
        sol += "Case #{}: {}\n".format(i+1, solve_case(list(reversed(list(cases[i])))))

    with open(INPUT_FILE.replace('.in','.out'), 'w') as fh:
        fh.write(sol)

if __name__ == '__main__':
    main()
