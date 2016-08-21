# python 3.4 !!

from functools import lru_cache
#

num_trials = int(input())

lookup = ['P','R','S']


def get_winner(a):
    asum = sum(a)
    if asum == 1:
        if a[0] == 1:
            return 0
        if a[1] == 1:
            return 1
        if a[2] == 1:
            return 2

    p = [0,0,0]
    for i in range(0,3):
        p[i] = asum // 2- a[(i+2)%3] # number of games where i beats i+1 wins

    if any(j < 0 for j in p):
        return -1

    return get_winner(p)

@lru_cache(maxsize = None)
def get_first_from_winner(winner, rounds):

    if rounds == 0:
        return lookup[winner]

    if rounds == 1:
        if winner == 2:
            return lookup[0] + "" + lookup[2]
        else:
            return lookup[winner] + "" + lookup[winner+1]

    p1 = winner
    p2 = (winner + 1) % 3
    
    ans1 = get_first_from_winner(p1, rounds-1)
    ans2 = get_first_from_winner(p2, rounds-1)
    
    return min(ans1 + ans2, ans2 + ans1)

    for i in range(0, l//2):
        next1 = almost_best[2*i]
        next2 = almost_best[2*i+1]
        if next1 == 0:
            if next2 == 1:
                ans = ans + "PR"
            else:
                ans = ans + "PS"
        else:
            ans = ans + "RS"

    return ans

def compute():
    a = [0,0,0]
    N,a[1],a[0],a[2] = map(int,input().split())

    winner = get_winner(a)

    if winner == -1:
        return "IMPOSSIBLE"

    return get_first_from_winner(winner, N)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
