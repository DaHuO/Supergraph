from collections import defaultdict
def solve(s):
    d = defaultdict(int)
    for c in s:
            d[c] += 1
    '''
    0: Z
    1:
    2: W
    3:
    4: U
    5:
    6: X
    7:
    8:
    9: 

     FIVE NINE 
    '''
    res = []
    while d['Z'] > 0:
        for c in 'ZERO':
            d[c] -= 1
        res.append(0)

    while d['W'] > 0:
        for c in 'TWO':
            d[c] -= 1
        res.append(2)

    while d['U'] > 0:
        for c in 'FOUR':
            d[c] -= 1
        res.append(4)

    while d['X'] > 0:
        for c in 'SIX':
            d[c] -= 1
        res.append(6)

    while d['R'] > 0:
        for c in 'THREE':
            d[c] -= 1
        res.append(3)

    while d['O'] > 0:
        for c in 'ONE':
            d[c] -= 1
        res.append(1)

    while d['G'] > 0:
        for c in 'EIGHT':
            d[c] -= 1
        res.append(8)
    while d['S'] > 0:
        for c in 'SEVEN':
            d[c] -= 1
        res.append(7)

    while d['F'] > 0:
        for c in 'FIVE':
            d[c] -= 1
        res.append(5)

    while d['N'] > 0:
        for c in 'NINE':
            d[c] -= 1
        res.append(9)

    res.sort()
    return ''.join([str(r) for r in res])



def fmt(file):
    f = open(file, 'r')
    count = int(f.readline())
    case = 1

    for l in f.readlines():
        word = l.strip()
        print 'Case #%d: %s' % (case, solve(word))
        case += 1
    f.close()

fmt('A-large.in')