import sys
sys.stdout = open("out.txt", "w")


def solve(x):
    if x == 0:
        return "INSOMNIA"
    j = 1
    t = x
    check = {}
    for i in range(10):
        check[str(i)] = False
    while True:
        s = str(t)
        for c in s:
            if c in check:
                del check[c]
        if len(check) == 0:
            return t
        else:
            j = j + 1
            t = j * x

lines = []

with open("A-large.in", "r") as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    ans = solve(int(lines[i]))
    print("Case #{}: {}".format(i, str(ans)))
