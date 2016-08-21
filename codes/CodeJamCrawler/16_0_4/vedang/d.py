t = int(input())

for i in range(1, t + 1):
    k, c, s = map(int, input().split())
    r = k ** (c - 1)
    arr = list(1 + j * r for j in range(k))
    print("Case #{}: {}".format(i, ' '.join(map(str, arr))))
