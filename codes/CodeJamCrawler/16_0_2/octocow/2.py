def solve(n):
    """
    -
    -+
    +-
    +++
    --+-
    """
    total = 0
    cmpare = len(n) * '+'
    while True:
        to_flip = 0
        if n == cmpare:
            return total

        while to_flip < len(n) and n[to_flip] == '-':
            # print to_flip, n[to_flip]
            to_flip += 1
        if to_flip == 0:
            while to_flip < len(n) and n[to_flip] == '+':
                to_flip += 1
        rest = n[to_flip:]
        what = '-' if n[0] == '+' else '+'
        n = what * to_flip + rest
        total += 1


t = int(raw_input())

for c in range(t):
    n = str(raw_input())
    print "Case #{}: {}".format(str(c + 1),
                                str(solve(n)))
