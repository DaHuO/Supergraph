import sys
import random

T = int(sys.stdin.readline())

WINNER = {
    ('P', 'R'): 'P',
    ('P', 'S'): 'S',

    ('R', 'P'): 'P',
    ('R', 'S'): 'R',

    ('S', 'P'): 'S',
    ('S', 'R'): 'R',
}

def has_winner(ordering):
    curr = ordering
    while len(curr) > 1:
        next = []
        for i in range(len(curr)/2):
            if curr[2*i] == curr[2*i+1]:
                return False
            next.append(WINNER[(curr[2*i], curr[2*i+1])])
        curr = next
    return True

def find_winner(o, p, r, s):
    if not p and not r and not s:
        if has_winner(o):
            return o
        else:
            return None

    if p:
        t = find_winner(o + 'P', p-1, r, s)
        if t:
            return t

    if r:
        t = find_winner(o + 'R', p, r-1, s)
        if t:
            return t

    if s:
        t = find_winner(o + 'S', p, r, s-1)
        if t:
            return t

    return None


for n in range(1, T+1):
    [N, R, P, S] = [int(x) for x in sys.stdin.readline().split()]

    o = find_winner('', P, R, S)
    
    if o:
        print "Case #{}: {}".format(n, o)
    else:
        print "Case #{}: {}".format(n, 'IMPOSSIBLE')
