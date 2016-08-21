def parse_input(items):
    return int(items[0])

def run(items):
    N = parse_input(items)
    #print N
    if N == 0:
        return "INSOMNIA"

    result = N
    digits = set()
    while True:
        p = result
        while (p != 0):
            digits.add(p % 10)
            p /= 10
        #print digits
        if (len(digits) == 10):
            break
        result += N
        
    return result


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    items = raw_input().split(" ")
    #if i != 2:
    #    continue
    result = run(items)
    print "Case #{}: {}".format(i, result)
    # check out .format's specification for more formatting options
