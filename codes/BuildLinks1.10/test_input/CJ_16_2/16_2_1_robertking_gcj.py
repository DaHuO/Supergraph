from collections import Counter
from random import shuffle
data = iter(open('A-large (1).in').read().splitlines())
cases = int(next(data))

x = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
x = map(Counter, x)

def solve(s2):
    s = Counter(s2)
    counts = [0]*len(x)
    stuff = list(enumerate(x))
    shuffle(stuff)
    for z, i in stuff:
        while all(s[j] for j in i):
            s -= i
            counts[z] += 1
    if len(s) == 0:
        return counts
    else:
        return solve(s2)


for case in range(1, cases + 1):
    s = next(data)
    counts = solve(s)
    ans = ''
    for i in range(len(counts)):
        ans += str(i)*counts[i]
    print "Case #%d: %s" % (case, ans)


