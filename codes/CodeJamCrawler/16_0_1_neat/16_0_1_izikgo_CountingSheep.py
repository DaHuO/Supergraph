def solve_case(case):
    if case == 0:
        return "INSOMNIA"

    cur = case
    seen = set(str(cur))
    while len(seen) < 10:
        cur += case
        seen.update(str(cur))

    return cur


def main():
    INPUT_FILE ="A-large.in"
    with open(INPUT_FILE) as fh:
        cases = [l.rstrip() for l in fh.readlines()[1:]]

    sol = ''
    for i in range(len(cases)):
        sol += "Case #{}: {}\n".format(i+1, solve_case(int(cases[i])))

    with open(INPUT_FILE.replace('.in','.out'), 'w') as fh:
        fh.write(sol)

if __name__ == '__main__':
    main()
