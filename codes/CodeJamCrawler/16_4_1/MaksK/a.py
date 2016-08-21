from itertools import permutations

def win(a, b):
    a, b = sorted([a, b])
    if a == "P":
        return b if b == "S" else a
    return "R"

t = int(input())
for case in range(1, t + 1):
    n, r, p, s = map(int, input().split())

    def ends(arr):
        for j in range(n):
            for i in range(2**(n - j - 1)):
                # print(2**(n - j)-1, n, i, j, arr)
                # print("COMP", j, i, "IS:", arr[2 * i], arr[2 * i + 1])
                if arr[2 * i] == arr[2 * i + 1]:
                    return False
                arr[i] = win(arr[2 * i], arr[2 * i + 1])
        return True
    result = "IMPOSSIBLE"
    for lineup in permutations(["P"]*p + ["R"]*r + ["S"]*s):
        # print(lineup, ends(list(lineup)))
        if ends(list(lineup)):
            result = "".join(lineup)
            break
    print("Case #{}: {}".format(case, result))
