import sys

def solve(stack):
    current = '+'
    flips = 0
    for l in stack[::-1]:
        if l != current:
            flips += 1
            current = l
    return str(flips)


lines = [x.strip() for x in sys.stdin.readlines()]

i = 1
lines = lines[1:]
for line in lines:
    solution = solve(line)
    print("Case #" + str(i) + ": " + solution)
    i += 1

