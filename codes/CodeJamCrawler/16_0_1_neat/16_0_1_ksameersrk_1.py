for index in range(1, int(input())+1):
    N = int(input().strip())
    if N == 0:
        print("Case #"+str(index)+": INSOMNIA")
        continue
    S = set(str(N))
    i = 1
    while len(S) != 10:
        i += 1
        S.update(str(N*i))

    print("Case #"+str(index)+": "+str(N*i))

