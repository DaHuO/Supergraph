



INPUT = 'A-small-attempt0.in'
OUTPUT = 'A-small-attempt0.out'

# INPUT = 'A-large.in'
# OUTPUT = 'A-large.out'

def match(p1, p2):
    if p1 == p2:
        return False
    else:
        s1 = min(p1, p2)
        s2 = max(p1, p2)
        if (s1 == 'P') and (s2 == 'R'):
            return 'P'
        elif (s1 == 'P') and (s2 == 'S'):
            return 'S'
        else: #(s1 == 'R') and (s2 == 'S'):
            return 'R'


def can_finish(lineup):
    old_lineup = lineup
    while len(old_lineup) > 1:
        current = []
        it = iter(old_lineup)
        for _ in xrange(len(old_lineup) / 2):
            p1 = next(it)
            p2 = next(it)
            res = match(p1, p2)
            if res:
                current.append(res)
            else:
                return False
        old_lineup = current
    return True



def gen_lineups(p, r, s, current):
    if p > 0:
        for l in gen_lineups(p-1, r, s, current + ['P']):
            yield l
    if r > 0:
        for l in gen_lineups(p, r-1, s, current + ['R']):
            yield l
    if s > 0:
        for l in gen_lineups(p, r, s-1, current + ['S']):
            yield l
    if p+r+s == 0:
        yield current



def find_lineup_bf(p, r, s):
    for l in gen_lineups(p, r, s, []):
        if can_finish(l):
            return ''.join(l)
    return 'IMPOSSIBLE'



with open(INPUT, 'r') as fin:
    T = int(fin.readline())
    with open(OUTPUT, 'w') as fout:
        for i in xrange(1, T + 1):
            n, r, p, s = map(int, fin.readline().split(' '))
            fout.write('Case #{}: {}\n'.format(i, find_lineup_bf(p, r, s)))
