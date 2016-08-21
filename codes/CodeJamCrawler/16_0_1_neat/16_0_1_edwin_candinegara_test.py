T = int(input())

def isNotFinished(count):
    for c in count:
        if not c:
            return True

    return False

def updateCount(N, count):
    s = str(N)
    for d in s:
        t = int(d)
        count[t] = True

    return count

for i in range (1, T + 1):
    count = [False for k in range (0, 10)]
    N = int(input())
    M = N

    if N == 0:
        print("Case #{}: {}".format(i, "INSOMNIA"), end="\n")
        continue

    while isNotFinished(count):
        count = updateCount(N, count)
        N += M

    print("Case #{}: {}".format(i, N - M), end="\n")
