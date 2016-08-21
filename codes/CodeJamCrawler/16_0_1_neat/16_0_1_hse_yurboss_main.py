T = int(input())

def solution(n):
    if n == 0:
        return "INSOMNIA"
    used = [False] * 10
    res = n
    while True:
        t = res
        while t != 0:
            used[t % 10] = True
            t //= 10
        if False not in used:
            break
        res += n
    return res

for test in range(1, T + 1):
    n = int(input())
    print("Case #{0}: {1}".format(test, solution(n)))
