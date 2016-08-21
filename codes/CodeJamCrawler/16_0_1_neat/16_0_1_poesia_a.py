T = int(input())

for i in range(1, T+1):
    N = int(input())
    ans = ""
    if N == 0:
        ans = "INSOMNIA"
    else:
        s = set(str(N))
        inc = N
        while len(s) < 10:
            N += inc
            s.update(set(str(N)))
        ans = str(N)

    print("Case #{}: {}".format(i, ans))
