import fileinput, sys

def digits(in_string):
    d = []
    for char in in_string:
        d.append(char)
    return d

def solve(n):
    if n == 0:
        return "INSOMNIA"

    current = 0
    seen = set()
    while len(seen) < 10:
        current += n
        for d in digits(str(current)):
            seen.add(d)
    return current

index = 0
seen = set()
for line in fileinput.input():
    index += 1
    if index == 1:
        continue
    print("Case #%d: %s" % (index - 1, solve(int(line))))
