import os
from random import choice


CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def read_test(f):
    with open(f, 'r') as ifs:
        for case in ifs.read().split('\n')[1:]:
            if case.strip():
                yield map(int, case.strip().split())


def generate(length):
    while True:
        b = [1,] + [choice([0, 1]) for _ in range(length - 2)] + [1,]
        s = ''.join(map(str, b))
        ok = True
        divs = []
        for base in range(2, 11):
            x = int(s, base)
            for d in range(2, min(300, x)):
                if x % d == 0:
                    divs.append(d)
                    break
            else:
                ok = False
        if ok:
            return [s] + divs
    return []
            


def solve_case(case):
    n, j = case
    res = []
    used = set()
    while len(res) < j:
        candidate = generate(n)
        if candidate[0] not in used:
            used.add(candidate[0])
            res.append(candidate)
    return res


def solve(cases):
    for case in cases:
        yield solve_case(case)
           

def save(f, asnwers):
    with open(f, 'w') as ofs:
        for case, ans in enumerate(asnwers):
            ofs.write('Case #%d:\n' % (case + 1))
            for lst in ans:
                ofs.write('%s\n' % ' '.join(map(str, lst)))


def main():
    for f in os.listdir(CUR_DIR):
        if f.startswith('C') and f.endswith('.in') or f == 'input.in':
            print(f)
            tests = read_test(f)
            answers = solve(tests)
            save(CUR_DIR + os.path.sep + f.replace('.in', '.out'), answers)
            print('Done!')


if __name__ == '__main__':
    main()
