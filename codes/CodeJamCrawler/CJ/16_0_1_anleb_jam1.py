t = int(input())
for i in range(1, t+1):
    print("Case #", i, ": ", sep='', end='')
    n = int(input())
    s = set()
    f = 1
    for i in range(1, 100):
        s = s.union(set(str(n*i)))
        if len(s) == 10:
            print(n*i)
            f = 0
            break
    if f:
        print("INSOMNIA")
