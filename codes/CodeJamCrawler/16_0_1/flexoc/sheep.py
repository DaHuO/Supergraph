T = int(input())

for t in range(T):
    N = int(input())
    l = [0 for i in range(10)]
    if N == 0:
        print("Case #%d: INSOMNIA" % (t + 1))
        continue
    for c in str(N):
        l[int(c)] += 1
    i = 1
    while not all(x > 0 for x in l):
        i += 1
        for c in str(N * i):
            l[int(c)] += 1
    print("Case #%d: %d" % (t + 1, N * i))



