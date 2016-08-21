import sys


input = sys.stdin.read().strip().split("\n")[1:]

def flip(p):
    d = {"+": "-", "-": "+"}
    r = p[::-1]
    return ''.join([d[i] for i in r])

def flips(p):
    # some heuristics
    if len(p) == 1:
        if p == "-":
            return 1
        else:
            return 0
    if len(p) == 2:
        if p[0] == "-":
            return 1
        if p[1] == "-":
            return 2
        else:
            return 0

    lenp = len(p)

    if sum(1 for i in p if i == "+") == lenp:
        return 0

    if sum(1 for i in p if i == "-") == lenp:
        return 1

    # check the rest
    prev = p[0]
    moves = 0
    checksum = sum(1 for i in p if i == "+")
    while checksum != lenp and checksum != 0:
        for e, c in enumerate(p):
            if c != prev:
                p = flip(p[:e])+p[e:]
                moves += 1
                prev = p[0]
                break
            prev = c
        checksum = sum(1 for i in p if i == "+")

    return moves if checksum == lenp else moves + 1


for case, p in enumerate(input):
    res = flips(p)
    print("Case #{0}: {1}".format((case+1), res))

