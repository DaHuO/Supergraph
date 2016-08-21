import sys


T = int(sys.stdin.readline())
for t in range(0,T):
    K,C,S = list(map(lambda x: int(x), sys.stdin.readline().split(" ")))

    if S == K:
        tiles = list(map(lambda x: str(x), range(1,S+1)))
        print("Case #%d: %s" % (t+1, " ".join(tiles)))
    elif 2*S <= K:
        print("Case #%d: IMPOSSIBLE" % (t+1))
    else:
        tiles = list(map(lambda x: str(x), range(2,2+S)))
        print("Case #%d: %s" % (t+1, " ".join(tiles)))
