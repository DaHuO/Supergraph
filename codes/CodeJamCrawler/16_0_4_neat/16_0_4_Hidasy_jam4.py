import sys
nl = sys.stdin.read().split("\n")[1:]
for case, data in enumerate(nl):
    res = 0
    try:
        K, C, S = [int(x) for x in data.split()]
    except:
        exit(0)
    if K == 1:
        res = 1
        print("Case #{}: {}".format(case+1, res))
        continue
    if K <= S:
        res = ' '.join([str(x) for x in range(1, S+1)])
    else:
        res = "IMPOSSIBLE"
    print("Case #{}: {}".format(case+1, res))
