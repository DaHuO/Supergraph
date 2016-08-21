import sys

filename = sys.argv[1]

def read_num_cases(f):
    return int(f.readline().strip())

def read_case(f):
    return f.readline().strip()

def min_flips(stack):
    flips = 0
    cur = stack[0]
    for ch in stack[1:]:
        if ch != cur:
            cur = ch
            flips += 1
    if cur == '-':
        flips += 1
    return flips

with open(filename, 'r') as f:
    num_cases = read_num_cases(f)
    for case in xrange(num_cases):
        stack = read_case(f)
        ans = min_flips(stack)
        print("Case #{}: {}".format(case + 1, ans))
