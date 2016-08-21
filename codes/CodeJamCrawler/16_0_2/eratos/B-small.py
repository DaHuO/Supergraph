import fileinput, sys

def solve(line):
    flips = 1
    first_char = True
    prev_char = ''
    for char in line[:-1]:
        if first_char:
            first_char = False
            prev_char = char
        if char == prev_char:
            continue
        flips += 1
        prev_char = char

    if prev_char == '+':
        return flips - 1
    return flips

index = 0
seen = set()
for line in fileinput.input():
    index += 1
    if index == 1:
        continue
    print("Case #%d: %s" % (index - 1, solve(line)))
