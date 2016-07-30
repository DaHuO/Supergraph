#!/usr/bin/env python3


def expand(s, rs, ss, ps, n):
    ans = None
    if s == 'S' and ps > 0:
        ans = 'PS' if n <= 2 else 'SP'
        ps -= 1
    elif s == 'P' and rs > 0:
        ans = 'PR'
        rs -= 1
    elif s == 'R' and ss > 0:
        ans = 'RS' if n == 1 else 'SR'
        ss -= 1
    return ans, rs, ss, ps


def generate(start, rs, ss, ps, n):
    ans = start
    while n > 0:
        # print(ans)
        ans1 = []
        for s in ans:
            s1, rs, ss, ps = expand(s, rs, ss, ps, n)
            if s1 is None:
                return None
            ans1 += [s1]
        ans = ''.join(ans1)
        n -= 1
    # print(ans)
    return ans


def get_possible_starts(r, p, s):
    ans = []
    if r > 0:
        ans.append('R')
    if s > 0:
        ans.append('S')
    if p > 0:
        ans.append('P')
    return ans


def solve(n, r, p, s):
    return min(list(filter(None, (generate(ss, r, s, p, n) for ss in get_possible_starts(r, p, s)))) or ['IMPOSSIBLE'])


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, r, p, s = [int(x) for x in input().split()]
        print('Case #{}: {}'.format(i, solve(n, r, p, s)))


if __name__ == '__main__':
    main()
