import fileinput

for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue
    pancakes = line.strip() + "+"
    flips = 0
    state = pancakes[0]
    for p in pancakes[1:]:
        if p != state:
            flips += 1
            state = p
    print "Case #{}: {}".format(e, flips)
