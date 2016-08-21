import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()

lines = contents.split('\n')

lines = lines[1:]

def flip(s, n):
    letters = [l for l in s]
    for i, let in enumerate(letters):
        if i >= n:
            break
        letters[i] = '+' if let == '-' else '-'

    return ''.join(letters)

def solved(seq):
    return all(s == '+' for s in seq)

def maj(seq):
    p =[s == '+' for s in seq]
    return len(p) / float(len(seq)) >= 0.5

map = {}
def solve(seq, seen=None):
    if seen is None:
        seen = set()
    if seq in map:
        return map[seq]
    if seq in seen:
        return 100000000

    seen.add(seq)
    if solved(seq):
        return 0
    letters = [l for l in seq]
    letters.reverse()
    for i, l in enumerate(letters):
        if l != '+':
            break

    seq = seq[:len(seq)-i]


    best = 10000000000
    for i in xrange(len(seq)):
        new_seq = flip(seq, i+1)
        if not maj(new_seq):
            continue
        new_seen = set(seen)
        n = solve(new_seq, new_seen)
        if n+1 < best:
            best = n+1

    map[seq] = best
    return best


for idx, l in enumerate(lines):
    if not l:
        continue
    out = str(solve(l))
    print 'Case #%d: %s' % (idx+1, out)
