from sys import stdin
from collections import Counter

T = int(next(stdin))

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def diff(C, lst):
    for i in range(len(lst)):
        if C[lst[i]] > 0:
            C[lst[i]] -= 1

for x in range(1, T+1):
    S = Counter(next(stdin).strip())

    X = []

    for _ in range(S["Z"]):
        X.append(0)
        diff(S, "ZERO")
    for _ in range(S["W"]):
        X.append(2)
        diff(S, "TWO")
    for _ in range(S["U"]):
        X.append(4)
        diff(S, "FOUR")
    for _ in range(S["X"]):
        X.append(6)
        diff(S, "SIX")
    for _ in range(S["G"]):
        X.append(8)
        diff(S, "EIGHT")
    for _ in range(S["S"]):
        X.append(7)
        diff(S, "SEVEN")
    for _ in range(S["V"]):
        X.append(5)
        diff(S, "FIVE")
    for _ in range(S["T"]):
        X.append(3)
        diff(S, "THREE")
    for _ in range(S["O"]):
        X.append(1)
        diff(S, "ONE")
    for _ in range(S["I"]):
        X.append(9)
        diff(S, "NINE")

    y = "".join(map(str, sorted(X)))

    print("Case #{0}: {1}".format(x, y))

    if sum(S.values()) != 0:
        print("fail")
        break
