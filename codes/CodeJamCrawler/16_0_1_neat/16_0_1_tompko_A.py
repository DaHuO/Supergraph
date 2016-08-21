import sys

def digits(n):
    digs = set()
    while n > 0:
        digs.add(n % 10)
        n = n // 10
    return digs

def sheep(n):
    if n == 0:
        return "INSOMNIA"
    seen = set()
    num = 0
    while len(seen) < 10:
        num += n
        seen.update(digits(num))
    return num

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        num_cases = int(fin.readline())
        for i in range(num_cases):
            n = int(fin.readline())
            print("Case #{}: {}".format(i+1, sheep(n)))
