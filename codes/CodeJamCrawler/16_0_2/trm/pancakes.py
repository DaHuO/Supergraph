from sys import argv

with open(argv[1]) as f:
    contents = [line for line in f]


def flip(cakes, n):
    return cakes[:n+1].replace('+','x')\
                      .replace('-', '+')\
                      .replace('x', '-') + cakes[n-1:]

def solve(inputValues : str) -> str:
    cakes = inputValues
    i = len(cakes)-1
    flips = 0
    while i >= 0:
        if cakes[i] == '-':
            cakes = flip(cakes, i)
            flips += 1
        i -= 1
    return flips



with open(argv[2], "w+") as f:
    contents = enumerate(contents)
    next(contents)
    for n, item in contents:
        f.write("Case #{}: {}\n".format(n, solve(item)))
