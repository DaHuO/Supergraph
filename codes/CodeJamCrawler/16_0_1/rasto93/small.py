import sys


def solve(t, N):
    if N == 0:
        print("Case #%d: INSOMNIA" % t)
        return

    digs = set()
    i = N
    while len(digs) != 10:
        num = i
        while num > 0:
            digs.add(num % 10)
            num //= 10
        i += N

    print("Case #%d: %d" % (t, i - N))

T = int(input())

for t, N in enumerate(sys.stdin):
    solve(t + 1, int(N))
