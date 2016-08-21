from sys import argv
import os

def solve_sheep(in_file):
    inp = open(in_file)
    root, ext = os.path.splitext(in_file)
    out = open(root + ".out", 'w')
    n_cases = int(inp.readline())
    for case in range(n_cases):
        sheep_number = sheep(int(inp.readline()))
        out.write("Case #{}: {}\n".format(case + 1, sheep_number))


def sheep(n):
    if n == 0:
        return "INSOMNIA"

    seen = set(str(n))
    num = n
    while len(seen) < 10:
        num += n
        seen = seen.union(list(str(num)))

    return num


if __name__ == "__main__":
    solve_sheep(argv[1])