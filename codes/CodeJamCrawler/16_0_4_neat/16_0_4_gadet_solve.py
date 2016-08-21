import sys

data = sys.stdin.read().strip()
cases = data.split('\n')[1:]

for index, case in enumerate(cases, start=1):
    searches = "IMPOSSIBLE"
    k, c, s = map(int, case.split(' '))
    if c == 1: # complexity 1 means you have to check every tile
        if k == s:
            searches = range(1,k+1)
    else:
        searches = []
        for i in range(k):
            #searches.append(i * (k ** (c - 1)) + c)
            searches.append(i+1)
    print "Case #{}: {}".format(index, ' '.join(map(str, searches)) if isinstance(searches, list) else searches)

