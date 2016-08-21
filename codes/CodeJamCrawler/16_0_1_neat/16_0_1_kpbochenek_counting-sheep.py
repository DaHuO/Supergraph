
T = int(input())

for i in range(T):
    N = int(input())
    if N == 0:
        result = "INSOMNIA"
    else:
        missing = [True for i in range(10)]
        count = 10
        iterx = 1
        while count > 0:
            for l in str(iterx * N):
                lx = int(l)
                if missing[lx] == True:
                    missing[lx] = False
                    count -= 1
            iterx += 1
        result = (iterx - 1) * N

    print("Case #" + str(i+1) + ": " + str(result))
