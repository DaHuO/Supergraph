from sys import stdin

def flip(pancakes):
    return "".join("+" if x == "-" else "-" for x in pancakes)

def solve(pancakes):
    if pancakes == "+":
        return 0
    if pancakes == "-":
        return 1

    if pancakes[-1] == "+":
        return solve(pancakes[:-1])
    if pancakes[-1] == "-":
        return 1 + solve(flip(pancakes[:-1]))

T = int(next(stdin))

for i, pancakes in zip(range(1, T+1), stdin):
    print("Case #%s: %s" % (i, solve(pancakes.strip())))
