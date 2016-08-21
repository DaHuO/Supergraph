import sys

def solve(n):
    if n == 0: return "INSOMNIA"
    found = set()
    i = 1
    while len(found) < 10:
        v = n * i
        i += 1
        for letter in str(v):
            found.add(letter)
    return str(n * (i - 1))

lines = [x.strip() for x in sys.stdin.readlines()]

i = 1
lines = lines[1:]
for line in lines:
    number = int(line)
    solution = solve(number)
    print("Case #" + str(i) + ": " + solution)
    i += 1

