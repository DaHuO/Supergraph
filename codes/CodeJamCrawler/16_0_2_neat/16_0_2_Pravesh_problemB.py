__author__ = 'pravesh'

file = open("B-large.in", "r").readlines()
T = int(file.pop(0))
i = 1

def get_flip_count(S):
    if '-' not in S:
        return 0
    flips = 1
    last_seen = S[0]
    for s in S[1:]:
        if s != last_seen:
            flips += 1
            last_seen = s
    if S[-1] == '+':
        flips -= 1
    return flips

while i <= T:
    S = file.pop(0)
    print("Case #%d:" % i, get_flip_count(S.strip()))
    i += 1
