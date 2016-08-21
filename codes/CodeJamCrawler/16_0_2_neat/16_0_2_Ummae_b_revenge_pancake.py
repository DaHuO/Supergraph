import sys
rl = lambda: sys.stdin.readline().strip()

def greedy(s):
    size = len(s)
    ans = [1 for i in range(size)]
    ret = 0
    while s:
        right = s[-1]
        if right:
            s = s[:-1]
            # print 'a', s
            continue
        leftmost = s[0]
        if not leftmost:
            ret += 1
            s = [c ^ 1 for c in s][::-1]
            # print 'b', s
            continue
        near_zero = -1
        for i in range(0, len(s) - 1):
            if s[i]:
                near_zero = i + 1
        ls = [c ^ 1 for c in s[:near_zero]][::-1]
        rs = s[near_zero:]
        # print near_zero, s
        s = ls + rs
        ret += 1
        # print 'c', s
    return ret

T = int(rl())
for tcase in range(1, T + 1):
    s = [1 if c == '+' else 0 for c in rl()]
    s += [1 for i in range(100)]
    s = s[:100]
    print 'Case #%d: %d' % (tcase, greedy(s))
