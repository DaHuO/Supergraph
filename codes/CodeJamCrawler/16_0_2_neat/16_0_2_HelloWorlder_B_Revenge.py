def parse_input(items):
    return items[0]

def run(items):
    pancakes = parse_input(items)
    #print pancakes

    last_pancake = None
    flips = 0
    i = 0
    while i < len(pancakes):
        p = pancakes[i]
        if p == '-':
            if last_pancake == '-':
                flips += 0
            elif i == 0:
                flips += 1
            else:
                flips += 2
        last_pancake = p
        i += 1
    return flips


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    items = raw_input().split(" ")
    result = run(items)
    print "Case #{}: {}".format(i, result)
    # check out .format's specification for more formatting options
