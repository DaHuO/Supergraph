from sys import stdin

T = int(next(stdin))

for i, line in zip(range(1, T+1), stdin):
    line = line.strip()
    s = line[0]
    for c in line[1:]:
        if c < s[0]:
            s = s + c
        else:
            s = c + s
    print("Case #{0:d}:".format(i), s)
