
def solve(i):
    if i == 0:
        return "INSOMNIA"
    c = set(str(i))
    current = i
    while len(c) < 10:
        current += i
        c.update(str(current))
    return current

if __name__ == '__main__':
    testcases = int(raw_input())
    for t in xrange(testcases):
        print "Case #{}: {}".format(t + 1, solve(int(raw_input())))