
anc = {
    'P' : ['P', 'R'],
    'R' : ['R', 'S'],
    'S' : ['P', 'S']
}
def solve(N, R, P, S):
    pos = []
    for opt in 'RPS':
        layers = [[anc[opt]]]
        for i in xrange(1, N):
            layers.append(map(lambda letter : anc[letter], sum(layers[i-1], [])))
        lineup = sum(layers[len(layers) - 1], [])
        r, p, s = [lineup.count('R'), lineup.count('P'), lineup.count('S')]
        if r == R and p == P and s == S:
            pos.append(layers[len(layers) - 1])

    if len(pos) == 0:
        return "IMPOSSIBLE"

    sorted_lineups = []
    for p in pos:
        cur = p
        for layer in xrange(N - 1):
            merged = []
            for i in xrange(len(cur) / 2):
                tmp = [cur[2 * i] , cur[2 * i + 1]]
                tmp.sort(key = lambda x : "".join(x))
                merged.append(sum(tmp, []))
            cur = merged
        sorted_lineups.append(cur)
    sorted_lineups.sort(key = lambda x : x[0])
    print sorted_lineups
    rv = "".join(sum(sorted_lineups[0], []))
    assert(len(rv) == 2**N)
    return rv

def read1(f):
    l = f.readline().strip()
    return map(int, l.split())