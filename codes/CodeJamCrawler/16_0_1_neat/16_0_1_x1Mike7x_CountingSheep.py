import os


CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def read_test(f):
    with open(f, 'r') as ifs:
        for case in ifs.read().split('\n')[1:]:
            try:
                yield int(case.strip())
            except ValueError:
                pass


def solve_case(case):
    if case == 0:
        return 'INSOMNIA'
    w = [0] * 10
    n = case
    for _ in range(1000):
        for c in str(n):
            w[int(c)] = 1
        if sum(w) == 10:
            return n
        n += case
    assert False
    return 'INSOMNIA'


def solve(cases):
    for case in cases:
        yield solve_case(case)
            

def save(f, asnwers):
    with open(f, 'w') as ofs:
        for case, ans in enumerate(asnwers):
            ofs.write('Case #%d: %s\n' % (case + 1, str(ans))) 


def main():
    for f in os.listdir(CUR_DIR):
        if '.in' in f and os.path.isfile(CUR_DIR + os.path.sep + f):
            print(f)
            tests = read_test(f)
            answers = solve(tests)
            save(CUR_DIR + os.path.sep + f.replace('.in', '.out'), answers)
            print('Done!')


if __name__ == '__main__':
    main()
