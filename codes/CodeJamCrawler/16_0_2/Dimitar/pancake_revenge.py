from itertools import groupby
from sys import stdin, stdout, stderr

def solve(s):
    flips = len(list(groupby(s))) - 1
    f = s[0]
    odd = flips & 1
    last = (f == '+') * (odd) + (f == '-') * (not odd)
    flips += last
    return flips


if __name__ == "__main__":
    T = int(stdin.readline().strip())
    for t in range(1, T + 1):
        S = stdin.readline().strip()
        ans = solve(S)
        stdout.write("Case #{0}: {1}\n".format(t, ans))

