import jam

def solve(case):
    N = case.readInt()
    if N == 0:
        return "INSOMNIA"
    k = 1
    seen = set()
    while k < 100:
        n = N * k
        for digit in str(n):
            seen.add(int(digit))
        if len(seen) == 10:
            return n
        k += 1
    return "INSOMNIA"

jam.run("A-large.in", solve)
