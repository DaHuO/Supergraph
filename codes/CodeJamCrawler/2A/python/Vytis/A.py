#!/usr/bin/env python3

TEST = 'large'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)

q = {
    'P': ('P', 'R'),
    'R': ('R', 'S'),
    'S': ('P', 'S'),
}

def plan(n, ch):
    if n == 0:
        return ch, int(ch == 'R'), int(ch == 'P'), int(ch == 'S')
    a, ra, pa, sa = plan(n-1, q[ch][0])
    b, rb, pb, sb = plan(n-1, q[ch][1])
    return min(a + b, b + a), ra + rb, pa + pb, sa + sb


def good_plans(n, r, p, s):
    for c in q.keys():
        pl, pr, pp, ps = plan(n, c)
        if (pr, pp, ps) == (r, p, s):
            yield pl

def run(n, r, p, s):
    return min(good_plans(n, r, p, s), default='IMPOSSIBLE')


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n, r, p, s = map(int, fin.readline().split())
            res = run(n, r, p, s)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()
