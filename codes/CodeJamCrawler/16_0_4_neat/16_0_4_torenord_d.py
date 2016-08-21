from sys import stdin

T = int(next(stdin))

for i, line in zip(range(1, T+1), stdin):
    K, C, S = map(int, line.strip().split(" "))
    print("Case #%s: %s" % (i, " ".join(map(str, range(1, S+1)))))
