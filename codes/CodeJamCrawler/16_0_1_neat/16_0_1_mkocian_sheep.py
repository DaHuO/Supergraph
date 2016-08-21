T = int(input().strip())

for t in range(T):
    n = int(input().strip())

    if n == 0:
        print("Case #{}: INSOMNIA".format(t+1))
        continue

    s = set()
    i = 1
    while len(s) < 10:
        s = s.union(set(str(n*i)))
        if len(s) == 10:
            print("Case #{}: {}".format(t+1, n*i))
        i += 1
