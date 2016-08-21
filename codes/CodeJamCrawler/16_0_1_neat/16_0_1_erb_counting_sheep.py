


def count(N):
    if N == 0:
        return "INSOMNIA"
    s = set()
    i = 0
    while len(s) < 10:
        i += 1
        [s.add(c) for c in str(N*i)]
    return N*i


n = int(input())
for i in range(n):
    N = int(input())
    print("Case #{}: {}".format(i+1, count(N)))

