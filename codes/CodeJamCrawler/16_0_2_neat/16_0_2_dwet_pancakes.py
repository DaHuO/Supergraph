
def flip(stack, index):
    flipped = [x for x in stack[:index + 1]][::-1]
    # actually flip
    for i, x in enumerate(flipped):
        if x == "-":
            flipped[i] = "+"
        else:
            flipped[i] = "-"
    return flipped + stack[index + 1:]


assert flip(["-", "-", "+", "-"], 3) == ["+", "-", "+", "+"]
assert flip(["+", "-", "+", "+"], 1) == ["+", "-", "+", "+"]
assert flip(["+", "-", "+", "+"], 0) == ["-", "-", "+", "+"]
assert flip(["-", "-", "+", "+"], 1) == ["+", "+", "+", "+"]

cases = int(raw_input())
for case in xrange(1, cases + 1):
    stack = [x for x in raw_input().strip()]

    flips = 0
    while not all(x == "+" for x in stack):
        flips += 1
        i = len(stack) - 1
        while stack[i] == "+":
            i -= 1

        if stack[0] == "+":
            # Can't be too greedy, find a good place to setup the next flip
            while stack[i] == "-":
                i -= 1
        stack = flip(stack, i)

    print "Case #%s: %s" % (case, flips)
