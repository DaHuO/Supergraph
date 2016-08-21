import sys

filename = sys.argv[1]

def read_num_cases(f):
    return int(f.readline().strip())

def read_case(f):
    return f.readline().strip()

def solve(S):
    win = S[0]
    for ch in S[1:]:
        if ch >= win[0]:
            win = ch + win
        else:
            win = win + ch
    return win

with open(filename, 'r') as f:
    num_cases = read_num_cases(f)
    for case in xrange(num_cases):
        p = read_case(f)
        ans = solve(p)
        print("Case #{}: {}".format(case + 1, ans))
