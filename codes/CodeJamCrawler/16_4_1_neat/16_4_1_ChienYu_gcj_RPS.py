from sys import stdin

def players(win):
    player = ['R', 'P', 'S']
    for i in xrange(N):
        y = [''] * 3
        for i in xrange(3):
            if player[i] < player[(i-1)%3]:
                y[i] = player[i] + player[(i-1)%3]
            else:
                y[i] = player[(i-1)%3] + player[i]
        player = y[:]

    return player[win]

def each_case(N, R, P, S):
    win, lose, loselose = 1, 1, 0
    for i in xrange(N-1):
        win, lose, loselose = loselose+win, win+lose, lose + loselose

    if (R, P, S) == (win, loselose, lose):  return players(0)
    if (R, P, S) == (lose, win, loselose):  return players(1)
    if (R, P, S) == (loselose, lose, win):  return players(2)
    return 'IMPOSSIBLE'

T = int(stdin.readline())
for t in xrange(1,T+1):
    N, R, P, S = map(int, stdin.readline().split())
    print 'Case #{}: {}'.format(t, each_case(N, R, P, S))
