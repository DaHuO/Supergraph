import fileinput


def fractiles(l):
    (k, c, s) = [int(x) for x in l.split(' ')]
    return " ".join(str(i) for i in range(1, k + 1))


lines = [l.strip() for l in fileinput.input()]
for (i, l) in enumerate(lines[1:]):
    print("Case #{}: {}".format(i + 1, fractiles(l)))
