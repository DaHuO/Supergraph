
from itertools import permutations

casen = int(input())

table = {'PR':'P','RP':'P', 'RS':'R','SR':'R', 'SP':'S', 'PS':'S' }

def play(lineup):
    if len(lineup) == 1:
        return True
    nextround = []
    for i in range(0, len(lineup), 2):
        if lineup[i] == lineup[i+1]:
            return False
        nextround.append( table[lineup[i]+lineup[i+1]] )
    return play(nextround)


for casei in range(1, casen+1):
    N, R, P, S = [int(x) for x in input().split(' ')]
    players = ['P']*P + ['R']*R + ['S']*S
    ans = "IMPOSSIBLE"
    for perm in permutations(players):
        if play(perm):
            ans = "".join(perm)
            break
    print("Case #",casei,": ",ans,sep="")
