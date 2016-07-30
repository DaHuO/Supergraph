from collections import deque


P, R, S = 0, 1, 2
match = {0: [P, R], 1: [R, S], 2: [P, S]}
tr = {0: 'P', 1: 'R', 2: 'S'}


def check(n, depth):
    t = deque()
    t.append(n)
    for d in range(depth):
        for i in range(2**d):
            t += match[t.popleft()]
    return [t, t.count(R), t.count(P), t.count(S)]


def sort_solution(t, n):
    if n == 1:
        return t
    l = len(t)
    t1 = sort_solution(t[:l//2], n - 1)
    t2 = sort_solution(t[l//2:], n - 1)
    if t1 < t2:
        return t1 + t2
    else:
        return t2 + t1


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, *rps = list(map(int, input().split()))
        print('Case #%d: ' % (case,), end='', sep='')
        tp = check(P, n)
        rt = check(R, n)
        ts = check(S, n)
        opts = []
        if rps == tp[1:]:
            opts.append(tp[0])
        if rps == rt[1:]:
            opts.append(rt[0])
        if rps == ts[1:]:
            opts.append(ts[0])

        if len(opts) == 0:
            print('IMPOSSIBLE')
        else:
            for i in range(len(opts)):
                opts[i] = sort_solution(list(opts[i]), n)
            sorted(opts)
            print(''.join(tr[x] for x in opts[0]))


if __name__ == "__main__":
    main()

