import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    print("Case #{}: ".format(t), end="")
    N = int(sys.stdin.readline())
    if (N == 0):
        print("INSOMNIA")
        continue
    found = [False] * 10
    n = 1
    while True:
        as_string = "{}".format(n*N)
        for c in as_string:
            found[int(c)] = True
        if all(found):
            print(n*N)
            break
        n += 1

