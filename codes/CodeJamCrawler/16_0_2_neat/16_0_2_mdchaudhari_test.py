def longest_streak(p, side):
    longest = 1
    for i in range(1, len(p) + 1):
        if filter(lambda x: x != side, p[:i]):
            break
        else:
            longest = i
    return longest

opposite = {'+': '-', '-': '+'}

with open('input.txt') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        p = f.readline()
        flips = 0
        while len(filter(lambda x: x == '-', p)):
            side = p[0]
            longest = longest_streak(p, side)
            p = opposite[side] * longest + p[longest:]
            flips += 1
        print "Case #{0}: {1}".format(i, flips)