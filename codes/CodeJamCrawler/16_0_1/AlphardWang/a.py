n = -1
c = 0
for line in open("A-large.in", mode="r"):
    if n == -1:
        n = int(line)
        continue
    c += 1
    print("Case #{0}: ".format(c), end="")
    d = int(line)
    if d == 0:
        print("INSOMNIA")
        continue
    k = set()
    ans = 1
    x = 0
    while True:
        x += d
        for ch in str(x):
            k.add(ch)
        if len(k) == 10:
            break
        ans += 1
    print(x)

