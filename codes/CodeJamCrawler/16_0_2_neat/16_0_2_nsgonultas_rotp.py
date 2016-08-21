import re


def flip(side):
    if side == "-":
        return "+"
    else:
        return "-"


with open("B-large.in") as f:
    tests = int(f.readline())
    cakes = map(str.strip, f.readlines())

results = list()

for cake in cakes:
    flips = 0
    while(cake != "+" * len(cake)):
        match = re.match("[+]+[-]+", cake)
        if(match):
            sides = match.group(0)
            cake = "".join(map(flip, sides)) + cake[len(sides):]
            flips += 1

        match = re.match("[-]+", cake)
        if(match):
            sides = match.group(0)
            cake = "".join(map(flip, sides)) + cake[len(sides):]
            flips += 1

    results.append(flips)

with open("B-large.out", "w") as f:
    for i in range(tests):
        f.write("Case #" + str(i + 1) + ": " + str(results[i]) + "\n")
