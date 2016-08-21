from sys import stdin, stdout, argv
from itertools import groupby

def pancake_flips(inp_file, out_file):
    inp = open(inp_file)
    out = open(out_file, 'w')
    n_cases = int(inp.readline())
    for case in range(n_cases):
        pancake = inp.readline()
        first_side_down = pancake[0] == '-'
        side_down_runs = [k for k, _ in groupby(pancake)].count('-')
        flips = side_down_runs * 2
        if first_side_down:
            flips -= 1

        out.write("Case #{}: {}\n".format(case + 1, flips))

if __name__ == '__main__':
    pancake_flips(argv[1], argv[2])
