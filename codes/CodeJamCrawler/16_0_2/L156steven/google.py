

def sheep(n):
    if n == 0:
        return "INSOMNIA"
    remaining = set(range(0, 10))
    for x in range(n, (100)*n, n):
        x_digits = x
        while x_digits is not 0:
            if not remaining:
                return x
            digit = x_digits % 10
            if digit in remaining:
                remaining.remove(digit)
            x_digits /= 10
        if not remaining:
            return x
    return "INSOMNIA"


def pancakes(input):
    stack = [True if i == '+' else False for i in input]
    stack.reverse()
    print stack
    not_flipped = True
    flips = 0
    for is_happy in stack:
        if is_happy == not_flipped:
            pass
        else:
            flips += 1
            not_flipped = not not_flipped

    return flips

#print pancakes('--+-')

"""
FILE = "input.in"
OUT = "out.out"
with open(FILE) as f:
    out = open(OUT,'w')
    f.readline()
    i = 1
    for line in f.readlines():
        out.write("Case #{}: {}\n".format(i, sheep(int(line))))
        i += 1
"""

FILE = "input.in"
OUT = "out.out"
with open(FILE) as f:
    out = open(OUT,'w')
    f.readline()
    i = 1
    for line in f.readlines():
        out.write("Case #{}: {}\n".format(i, pancakes(line.strip())))
        i += 1