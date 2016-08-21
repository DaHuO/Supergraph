# Solution to "Red Tape Committee" for Google Code Jam 2016
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
from itertools import combinations

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            n, k = [int(x) for x in f.readline().split()]
            yield n, k, [float(x) for x in f.readline().split()]

def compute(probs):
    yesprob = [0.0 for _ in range(len(probs))]
    yesprob[0] = 1.0
    for p in probs:
        for q in range(len(yesprob)-1, 0, -1):
            yesprob[q] = (1-p)*yesprob[q] + p*yesprob[q-1]
        yesprob[0] = (1-p)*yesprob[0]
    return yesprob[len(probs)/2]   

def solve(n, k, probs):
    best = 0.0
    for picks in combinations(range(n), k):
        testProbs = [p for i, p in enumerate(probs) if i in picks]
        t = compute(testProbs)
        if t > best:
            best = t
    return str(best)

with open(sys.argv[2], 'w') as f:
    for num, data in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(*data)))
