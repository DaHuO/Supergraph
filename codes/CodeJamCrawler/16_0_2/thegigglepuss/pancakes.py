import sys

def opposite(val):
    return '+' if val == '-' else '-'

def solve(count, line):
    solution = list('+' * len(line))
    if solution == line:
        return count, line
    last = line[0]
    for idx, c in enumerate(line):
        if c == last:
            line[idx] = opposite(c)
        else:
            break
    return solve(count + 1, line)

with open(sys.argv[1], 'r') as f:
    lines = int(f.readline())
    count = 1
    for line in f:
        answer = solve(0, list(line.rstrip()))
        print "Case #{}: {}".format(count, answer[0])
        count += 1

