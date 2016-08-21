def checkNumber(check, N):
    N = str(N)
    for i in N:
        check[int(i)] = True

    return all(check)


if __name__ == "__main__":
    times = int(input())

    for i in range(times):
        N = int(input())

        if N == 0:
            print("Case #%d: %s" % (i+1,"INSOMNIA"))
            continue

        Reset = N
        mul = 2
        retVal = N
        check = [False] * 10
        isDone = checkNumber(check, N)

        while not isDone:
            N = N * mul
            isDone = checkNumber(check, N)
            retVal = N
            N = Reset
            mul = mul + 1

        print("Case #%d: %d" % (i+1, retVal))
