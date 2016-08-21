import sys
from collections import defaultdict
# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt0.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(n, r, p, s):
    a = [0, 0, 1]
    for i in range(n):
        b = a[:]
        for j in range(3):
            b[j] += a[(j+1) % 3]
        a = b[:]
        b.sort()
    b.sort()
    if not sorted([r, p, s]) == b:
        return 'IMPOSSIBLE'
    u = [2]
    for i in range(n):
        v = []
        for l in u:
            v.extend([l, (l-1) % 3])
        u = v[:]
    c = [u.count(i) for i in range(3)]
    d = {'p':p, 'r': r, 's': s}
    for matching in ['psr', 'rps', 'srp']:
        ok = True
        for j in range(3):
            ok &= u.count(j) == d[matching[j]]
        if ok:
            m = matching
            break
    t = [m[k] for k in u]
    pow_n = 2 ** n
    block = 1
    while block < pow_n:
        for i in range(0, pow_n, 2 * block):
            if t[i:i+block] > t[i+block:i+2*block]:
                t[i:i + block], t[i + block:i + 2 * block] = t[i + block:i + 2 * block], t[i:i + block]
        block *= 2
    res = ''.join(t).upper()
    return res


def main():

    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        n, r, p, s = list(map(int, input().split()))
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it(n, r, p, s)
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)

if __name__ == '__main__':
    main()
1