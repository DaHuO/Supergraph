import sys

def solve(number):
    found = set()
    for i in range(0, 100):
        val = str((i + 1) * number)
        for c in val:
            found.add(c)
        if len(found) == 10:
            return val
    return 'INSOMNIA'

with open(sys.argv[1], 'r') as f:
    lines = int(f.readline())
    count = 1
    for line in f:
        start = long(line)
        answer = solve(start)
        print "Case #{}: {}".format(count, answer)
        count += 1

