def next_sheep(n):
    i = 1
    while True:
        yield n*i
        i += 1


def solve(n):
    if n == "0":
        return "INSOMNIA"
    seen = set()
    for sheep in next_sheep(int(n)):
        seen |= set(str(sheep))
        if len(seen) == 10:
            return sheep

n = int(input())
for i in range(n):
    print("Case #{}: {}".format(i+1, solve(input())))
