T = int(raw_input())

def solve(booleans, i, test=True):
    if i == len(booleans):
        return 0
    if booleans[i] == test:
        return solve(booleans, i + 1, test)
    return 1 + solve(booleans, i + 1, not test)

for t in range(1, T + 1):
    booleans = list(reversed(map(lambda x: x == '+', raw_input())))
    print 'Case #%d: %d' % (t, solve(booleans, 0))
