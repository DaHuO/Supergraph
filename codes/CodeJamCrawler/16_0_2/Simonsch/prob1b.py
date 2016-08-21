import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    line = sys.stdin.readline()
    line = line[::-1]
    last = '+'
    n = 0
    for c in line:
        if c != '+' and c != '-':
            continue
        if last != c:
            n = n+1
            last = c
    print("Case #{}: {}".format(t, n))
