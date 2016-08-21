import sys
from itertools import count

lines = open(sys.argv[1] + ".in", "rU").read().split("\n")
t, lines = int(lines[0]), lines[1:]

outfile = open(sys.argv[1] + ".out", "w")

for i in range(t):
    n = int(lines[i])
#    print("for", n)
    if n == 0:
        out = "INSOMNIA"
    else:
        seen = [False] * 10
        for j in count(1):
            for letter in str(n * j):
                seen[int(letter)] = True
#            print(n * j, list(map(int, seen)))
            if all(seen):
                out = n * j
                break
    print("Case #{}: {}".format(i + 1, out), file=outfile)

