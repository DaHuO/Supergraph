# Solution to "Rather Perplexing Showdown" for Google Code Jam 2016
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            yield [int(x) for x in f.readline().split()]

beats = {'R': 'S', 'P': 'R', 'S': 'P'}

def build(winner, n):
    current = winner
    results = []
    for _ in range(n):
        results.append(current)
        newCurrent = ''
        for player in current:
            newCurrent += player + beats[player]
        current = newCurrent
    results.append(current)
    return results

def sortBuild(results):
    for row in range(len(results)):
        r = results[row]
        group = 1
        while group <= len(r)/2:
            for p in xrange(0, len(r), 2*group):
                bit1 = r[p:p+group]
                bit2 = r[p+group:p+2*group]
                if bit2 < bit1:
                    r = r[:p] + bit2 + bit1 + r[p+2*group:]
            group *= 2
        results[row] = r

precalc = {}
for winner in ['R', 'P', 'S']:
    t = build(winner, 12)
    sortBuild(t)
    precalc[winner] = t

def solve(n, r, p, s):
    ans = ''
    for winner in ['R', 'P', 'S']:
        test = precalc[winner][n]
        if test.count('R') == r and test.count('P') == p and test.count('S') == s:
            if ans == '' or test < ans:
                ans = test
    if ans != '':
        return ans
    else:
        return 'IMPOSSIBLE'

with open(sys.argv[2], 'w') as f:
    for num, data in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(*data)))
