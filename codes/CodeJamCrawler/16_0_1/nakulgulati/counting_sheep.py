t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    num_set = set()

    if n == 0:
        print("Case #{}: {}".format(i, "INSOMNIA"))
        continue

    j = 0
    N = n
    sleep = False
    while not sleep:
        N = (j + 1) * n
        for d in str(N):
            num_set.add(int(d))
            if len(num_set) == 10:
                sleep = True
        j += 1

    print("Case #{}: {}".format(i, N))
