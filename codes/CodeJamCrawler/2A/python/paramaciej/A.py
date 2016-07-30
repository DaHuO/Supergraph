#!/usr/bin/env python3

cases = int(input())

allowed = ['pr', 'ps', 'rs']
winner = {
    'pr': 'p',
    'ps': 's',
    'rp': 'p',
    'rs': 'r',
    'sp': 's',
    'sr': 'r'
}

def can(plrs, pair):
    return plrs[pair[0]] > 0 and plrs[pair[1]] > 0

def use(plrs, pair):
    new_plrs = dict(plrs)
    for x in pair:
        new_plrs[x] -= 1
    return new_plrs

def tree(plrs, l):
    if sum(plrs.values()) == 0:
        return l if check(l) else None

    for pair in allowed:
        if can(plrs, pair):
            if len(l) % 2 == 1 and l[-1] == pair:
                continue
            appended = list(l)
            appended.append(pair)
            r = tree(use(plrs, pair), appended)
            if r:
                return r
    return None

def check(pairs):

    try:
        x = [winner[p] for p in pairs]
        if len(x) == 1:
            return True
        new =[x[2*i]+x[2*i+1] for i in range(len(x)//2)]
        return check(new);
    except KeyError:
        return False



for T in range(1, cases+1):
    N, R, P, S = [int(x) for x in input().split()]
    players = {'p': P, 'r': R, 's': S}
    
    r = tree(players, [])
    print("Case #{}: {}".format(T, ''.join(r).upper() if r else "IMPOSSIBLE"))

    
