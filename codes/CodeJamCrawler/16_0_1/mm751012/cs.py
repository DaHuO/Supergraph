import sys

rl = lambda: sys.stdin.readline().strip()

for case in range(int(rl())):
    N = int(rl())
    case = "Case #%d:" % (case+1)

    nums = [N]
    f = [False] * 10
    for i in map(int, list(str(N))):
        f[i] = True

    n = 0
    n_list = []
    while True:
        n += N
        if n in n_list:
            print case, "INSOMNIA"
            break
        n_list.append(n)

        for i in map(int, list(str(n))):
            f[i] = True

        if not False in f:
            print case, n
            break

