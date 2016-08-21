import itertools


def expand(seq, iters):
    out = seq
    in_seq = seq
    in_len = len(in_seq)
    for _ in range(iters):
        out = ""
        for s in seq:
            if s == 'L':
                out += in_seq
            else:
                out += 'G' * in_len
        seq = out
    return out


def pos(k, i, c):
    # print k, i, c
    return (k ** (c - 1) * i) + (i + 2)

tests = int(raw_input())

for test in xrange(1, tests + 1):
    k, c, s = [int(s) for s in raw_input().split(" ")]
    # for i in itertools.product("LG", repeat=k):
        # seq = ''.join(i)
        # expanded = expand(seq, c - 1)
        # print seq, expanded

    if k <= s:
        res = ' '.join(map(str, [i + 1 for i in range(k)]))
    if c == 1:
        if k > s:
            res = "IMPOSSIBLE"
        else:
            res = ' '.join(map(str, [i + 1 for i in range(k)]))
    else:
        if k > s * 2:
            res = "IMPOSSIBLE"
        else:
            i = [pos(k, i, c) if pos(k, i, c) <= k ** c else k ** c for i in range(0, k, 2)]
            res = ' '.join(map(str, i))

    print "Case #{}: {}".format(test, res)
