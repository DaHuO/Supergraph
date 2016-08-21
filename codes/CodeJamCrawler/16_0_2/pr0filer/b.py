p = 'b'


def solve(case):
    # print('case', case)
    count = len(case)
    if count == 1:
        if case == '-':
            return 1
        else:
            return 0
    else:
        flips = 0
        prev = case[0]
        for i in range(1, count):
            if prev != case[i]:
                flips += 1
            if i+1 == count and case[i] == '-':
                flips += 1
            prev = case[i]
        return flips

with open('%s.in' % p) as fin:
    with open('%s.out' % p, 'w+') as fout:
        cases = int(next(fin))
        for i in range(1, cases+1):
            case = next(fin)
            solution = 'Case #%s: %s\n' % (i, solve(case.strip()))
            # print('solution', solution)
            fout.write(solution)
