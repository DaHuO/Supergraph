T = int(input())

def best(N, whom):
    other = None
    if whom == "R":
        other = "S"
    elif whom == "P":
        other = "R"
    else:
        other = "P"
    if N == 1:
        return min(whom + other, other + whom)
    left = best(N - 1, whom)
    right = best(N - 1, other)
    return min(left + right, right + left)

for test in range(1, T + 1):
    N, R, P, S = [int(x) for x in input().split()]

    print("Case #%d: " % test, end="")
    answer = None

    pos = "RPS"
    for c in pos:
        aux = best(N, c)
        if aux.count('R') != R or aux.count('S') != S or aux.count('P') != P:
            continue
        if answer:
            answer = min(answer, aux)
        else:
            answer = aux
    if answer is None:
        print("IMPOSSIBLE")
    else:
        print(answer)
