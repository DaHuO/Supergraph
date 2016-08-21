import sys

T = int(input())

for i in range(1, T + 1):
    n = int(input())

    if n == 0:
        print("Case #{}: INSOMNIA".format(i))
        continue

    seen = {}

    m = 0
    while len(seen) < 10:
        m += n
        # sys.stderr.write("{} {}\n".format(n, m))
        s = str(m)
        for c in s:
            if c not in seen:
                seen[c] = True

    print("Case #{}: {}".format(i, m))
