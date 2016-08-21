import sys

def solve(n):
    if n == 0:
        return "INSOMNIA"
    seen = set()
    original_n = n
    while True:
        i = n
        # print(i)
        while i:
            seen.add(i % 10)
            i = int(i / 10)
        # print(seen)
        if len(seen) == 10:
            return n
        n += original_n


filename = sys.argv[1]

with open(filename) as f:
    f.readline()
    i = 1
    for line in f:
        print("Case #{}: {}".format(i, solve(int(line))))
        i += 1
