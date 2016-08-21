
def solve(case):
    if int(case) == 0:
        return 'INSOMNIA'
    required = range(0, 10)
    n = int(case)
    nn = case
    i = 1
    while(required):
        nn = str(n * i)
        nrs = [int(nn[x]) for x in range(0, len(nn))]
        i += 1
        required = [r for r in required if r not in nrs]
    return nn

with open('a.in') as fin:
    with open('a.out', 'w+') as fout:
        cases = int(next(fin))
        for i in range(1, cases+1):
            case = next(fin)
            solution = 'Case #%s: %s\n' % (i, solve(case.strip()))
            fout.write(solution)
