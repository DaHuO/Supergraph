
OPP = {
  'S': 'P',
  'P': 'R',
  'R': 'S',
}


def get_lineup(winner, N):
    lineup = [None] * (2**N)
    lineup[0] = winner
    fill_lineup(lineup, 0, len(lineup))
    return lineup

def fill_lineup(lineup, start, end):
    if end > start + 1:
        mid = (start+end) // 2
        lineup[mid] = OPP[lineup[start]]
        fill_lineup(lineup, start, mid)
        fill_lineup(lineup, mid, end)

def sort_lineup(lineup):
    i = 1 #stride
    while i < len(lineup):
        for k in range(0, len(lineup), i*2):
            if greater(lineup, k, lineup, k+i, i):
                lineup[k:k+i], lineup[k+i:k+2*i] = lineup[k+i:k+2*i], lineup[k:k+i]
        i *= 2

def greater(lineup1, k1, lineup2, k2, n):
    for j in range(n):
        if lineup1[k1+j] > lineup2[k2+j]:
            return True
        elif lineup1[k1+j] < lineup2[k2+j]:
            return False
    return False

def lineup_ok(lineup, R, P, S):
    return lineup.count('R')==R and lineup.count('S')==S and lineup.count('P')==P

def solve(N, R, P, S):
    best_lineup = None
    for winner in ['R', 'P', 'S']:
        lineup = get_lineup(winner, N)
        if lineup_ok(lineup, R, P, S):
            sort_lineup(lineup)
            if best_lineup is None or greater(best_lineup, 0, lineup, 0, len(lineup)):
                best_lineup = lineup
    return best_lineup

def run(name):
    f = open('{0}.in'.format(name), 'r')
    g = open('{0}.out'.format(name), 'w')

    T = int(f.readline())
    for t in range(T):
        N, R, P, S = [int(x) for x in f.readline().split()]
        lineup = solve(N, R, P, S)
        if lineup:
            g.write('Case #{0}: {1}\n'.format(t+1, ''.join(lineup)))
        else:
            g.write('Case #{0}: IMPOSSIBLE\n'.format(t+1))

    f.close()
    g.close()

if __name__ == '__main__':
    run('A-large')
