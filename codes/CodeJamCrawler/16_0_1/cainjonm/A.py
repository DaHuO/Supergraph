import sys

T = int(input())
for t in range(1, T+1):
    N = int(input())
    i = 0
    b = [0] * 10
    res = "INSOMNIA"

    #print("Working out ", N, file=sys.stderr)
    while True:
        cur = (i + 1) * N
        if cur == 0:
            break

        for x in str(cur):
            b[int(x)] = 1

        if sum(b) == 10:
            res = cur
            break

        i += 1
    #print("Done ", N, file=sys.stderr)
    print("Case #{0}: {1}".format(t, res))
