def digits(n):
    result = set()
    result.add(n % 10)
    n = n/10
    while (n > 0):
        result.add(n % 10)
        n = n/10
    return result


def solve(n):
    n = int(n)
    result = n
    digits_seen = set()
    if n == 0:
        return "INSOMNIA"
    while True:
        digits_seen |= digits(result)
        if len(digits_seen) == 10:
            return result
        result += n


def read_input():
    with open('A-large.in') as f:
        lines = list(f)
    # Skip the number of examples.
    instances = lines[1:]
    with open('output.txt', 'w') as f:
        solns = []
        for case, sol in enumerate(map(solve, instances), 1):
            soln = "Case #%(case)s: %(sol)s" % vars()
            print soln
            solns.append(soln)
        f.write('\n'.join(solns))
read_input()

#print solve(1692)