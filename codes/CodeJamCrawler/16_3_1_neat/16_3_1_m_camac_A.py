T = input()

def valid(P):
    s = sum(P)
    return all(y <= 0.5 * s for y in P)

def solve(N, P):
    left = sum(P)
    moves = []
    while sum(P):
        x, y = sorted(range(N), key=lambda i: P[i])[-2:]
        if P[x] and P[y]:
            Q = P[:]
            Q[x] -= 1
            Q[y] -= 1
            if valid(Q):
                P = Q
                moves.append(str(chr(ord('A') + x) + chr(ord('A') + y)))
                continue
        Q = P[:]
        Q[y] -= 1
        assert valid(Q)
        P = Q
        moves += chr(ord('A') + y)

    return ' '.join(moves)

for i in range(1, T + 1):
    N = input()
    P = map(int, raw_input().strip().split())
    print 'Case #{}: {}'.format(i, solve(N, P))
