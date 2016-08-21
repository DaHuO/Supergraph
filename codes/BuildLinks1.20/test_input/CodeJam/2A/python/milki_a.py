from collections import defaultdict

d = {}

def main():
    T = int(raw_input())
    gen('R', 12)
    gen('P', 12)
    gen('S', 12)
    # print d

    for i in xrange(T):
        N, R, P, S = map(int, raw_input().split())
        found = []
        for t in ('R', 'P', 'S'):
            st, cr, cp, cs = d[(t, N)]
            if cr != R or cp != P or cs != S:
                continue
            found.append(st)
        if not found:
            found.append('IMPOSSIBLE')
        found = sorted(found)
        # print N, R, P, S
        output(i, found[0])

def gen(l, n):
    global d
    ret = [l]
    for r in range(n):
        ret = go(ret)
        c_r = sum(1 for t in ret if t == 'R')
        c_p = sum(1 for t in ret if t == 'P')
        c_s = sum(1 for t in ret if t == 'S')
        d[(l, r+1)] = (''.join(bin_sort(ret)), c_r, c_p, c_s)

def bin_sort(l):
    if len(l) <= 2:
        return sorted(l)
    le = len(l) / 2
    left = l[:le]
    right = l[le:]

    if left < right:
        return bin_sort(left) + bin_sort(right)
    else:
        return bin_sort(right) + bin_sort(left)

def go(l):
    ret = []
    for t in l:
        if t == 'R':
            ret += ['R', 'S']
        if t == 'S':
            ret += ['P', 'S']
        if t == 'P':
            ret += ['P', 'R']
    return ret


def output(casenum, ret):
    print 'Case #%d: %s' % (casenum + 1, ret)


main()
