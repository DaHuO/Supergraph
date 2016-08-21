def solve(cakes):
    flips = 0

    if len(cakes) == 1:
        if cakes[0] == "-":
            return 1
        else:
            return 0

    for i in range(1, len(cakes)):
        if cakes[i] != cakes[i-1]:
            flips = flips + 1

    if cakes[len(cakes) - 1] == "-":
        flips = flips + 1

    return flips


cases = int(input())
for i in range(cases):
    case = input()
    print("Case #{}: {}".format(i+1, solve(case)))
