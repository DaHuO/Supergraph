from sys import argv

def fractal(in_file, out_file):
    inp = open(in_file)
    out = open(out_file, 'w')

    n_cases = int(inp.readline())
    for case in range(n_cases):
        orig_tiles, complexity, open_tiles = map(int, inp.readline().split())
        one_tile = orig_tiles ** (complexity - 1)
        if complexity == 1:
            one_tile = 0

        to_open = [(i-1)*one_tile + i for i in range(1, orig_tiles + 1)]
        out.write("Case #{}: {}\n".format(case + 1, " ".join(map(str, to_open))))

if __name__ == "__main__":
    fractal(argv[1], argv[2])