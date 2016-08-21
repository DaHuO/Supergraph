from itertools import permutations

match = {
    ('R', 'P'): 'P',
    ('P', 'S'): 'S',
    ('R', 'S'): 'R',
    ('S', 'R'): 'R',
    ('S', 'P'): 'S',
    ('P', 'R'): 'P',
    ('P', 'P'): None,
    ('S', 'S'): None,
    ('R', 'R'): None
}

T = int(input())
for I in range(1, T+1):
    n, r, p, s = [int(x) for x in input().split()]

    players = 'R'*r + 'P'*p + 'S'*s
    cor = []
    for row in permutations(players):
        row = list(row)
        cur = row[:]
        while len(cur) != 1:
            next = []
            for k in range(0, len(cur) // 2):
                a = cur[2*k]
                b = cur[2*k+1]
                next.append(match[(a, b)])
            if None in next:
                break
            cur = next
        if len(cur) == 1:
            cor.append(row)

    cor.sort()
    if len(cor):
        result = ''.join(cor[0])
    else:
        result = 'IMPOSSIBLE'

    print("Case #%d: %s" % (I, str(result)))
