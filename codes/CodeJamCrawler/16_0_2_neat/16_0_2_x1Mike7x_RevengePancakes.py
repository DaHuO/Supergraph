import os
from collections import deque


CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def read_test(f):
    with open(f, 'r') as ifs:
        for case in ifs.read().split('\n')[1:]:
            if case.strip():
                yield case.strip()


def brute_force(case):
    q = deque()
    used = set()
    n = len(case)
    par = dict()
    q.append((case, 0))
    used.add(case)
    par[case] = case
    while len(q) > 0:
        v, length = q.popleft()
        if v.count('+') == n:
            #path = [v, ]
            #while par[v] != v:
                #path.append(par[v])
                #v = par[v]
            #for i in path[::-1]:
                #print(i)
            #print('\n')
            return length
        for i in range(n):
            x = [c for c in v]
            ch = [('+', '-')[c == '+'] for c in x[:i+1][::-1]]
            x = ch + x[i+1:]
            s = ''.join(x)
            if s not in used:
                par[s] = v
                used.add(s)
                q.append((s, length + 1))          
    return int(1e9)


def dif(case):
    a = 1
    for x, y in zip(case, case[1:]):
        if y != x:
            a += 1
    if case[-1] == '+':
        a -= 1
    return a


def check(case):
    assert(dif(case) == brute_force(case))


def solve_case(case):
    if len(case) < 12:
        check(case)
    return dif(case)


def solve(cases):
    for case in cases:
        yield solve_case(case)
           

def save(f, asnwers):
    with open(f, 'w') as ofs:
        for case, ans in enumerate(asnwers):
            ofs.write('Case #%d: %s\n' % (case + 1, str(ans))) 


def main():
    for f in os.listdir(CUR_DIR):
        if f.startswith('B') and f.endswith('e.in') or f == 'input.in':
            print(f)
            tests = read_test(f)
            answers = solve(tests)
            save(CUR_DIR + os.path.sep + f.replace('.in', '.out'), answers)
            print('Done!')


if __name__ == '__main__':
    main()
