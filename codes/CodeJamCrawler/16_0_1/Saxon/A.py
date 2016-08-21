cases = int(input())
for c in range(cases):
    seen = {}
    N = int(input())
    last = N
    if (N == 0):
        print("Case #{}: INSOMNIA".format(c+1))
        continue

    i = 1
    while True:
        n = N * i
        last = n
        for ch in str(n):
            seen[ch] = True
        if len(seen) == 10:
            break
        i = i + 1
    print("Case #{}: {}".format(c+1, str(last)))
