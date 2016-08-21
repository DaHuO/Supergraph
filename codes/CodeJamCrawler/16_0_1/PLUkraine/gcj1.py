def getDigits(N):
    ans = set()
    while N > 0:
        ans.add(N % 10)
        N //= 10
    return ans


def brute(N):
    if N == 0:
        return "INSOMNIA"
    x = N
    soFar = getDigits(x)
    while len(soFar) != 10:
        x += N
        soFar = soFar.union(getDigits(x))
        # print(str(soFar)+" "+str(x))
    return x

T = int(input())
for i in range(T):
    inN = int(input())
    print("Case #{0}: {1}".format(i+1, brute(inN)))
