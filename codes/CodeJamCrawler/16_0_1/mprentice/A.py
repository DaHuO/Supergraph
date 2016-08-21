import sys

filename = sys.argv[1]

def read_num_cases(f):
    return int(f.readline().strip())

def read_case(f):
    return int(f.readline().strip())

def allnums(N):
    if N == 0:
        return "INSOMNIA"
    s = set(range(10))
    i = 0
    while len(s) > 0:
        i = i + 1
        for ch in str(i * N):
            if int(ch) in s:
                s.remove(int(ch))
    return str(i * N)

with open(filename, 'r') as f:
    num_cases = read_num_cases(f)
    for case in xrange(num_cases):
        N = read_case(f)
        ans = allnums(N)
        print("Case #{}: {}".format(case + 1, ans))
