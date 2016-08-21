import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()

lines = contents.split('\n')
lines = lines[1:]

def counts(l):
    d = {}
    for i in l:
        d.setdefault(i, 0)
        d[i] += 1
    return d

def index(k, c, args):
    assert len(args) == c
    # args should be 0 indexed (0 - k-1)
    assert [i >= 0 and i < k for i in args]
    assert len(args) == len(set(args)) or (counts(args)[0] > 0 and len(set(counts(args).values())) <= 2)
    # return them 0-indexed
    ret = 0
    for i, a in enumerate(args):
        ret += a * k ** (c - i - 1)
    return ret

def indices(k, c, s):
    if s <= 0:
        return []
    inds = range(k)
    idxs = []
    while s > 0 and len(inds):
        next_args = []
        for _ in xrange(c):
            if len(inds) == 0:
                next_args.append(0)
            else:
                next_args.append(inds.pop(0))

        idxs.append(index(k, c, next_args))
        s -= 1

    if len(inds):
        return []
    else:
        return idxs

for idx, l in enumerate(lines):
    if not l:
        continue
    k, c, s = l.split(' ')
    idxs = indices(int(k), int(c), int(s))
    if len(idxs):
        out = ' '.join([str(i+1) for i in idxs])
    else:
        out = 'IMPOSSIBLE'

    print 'Case #%d: %s' % (idx+1, out)
