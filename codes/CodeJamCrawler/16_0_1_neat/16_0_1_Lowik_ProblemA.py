__author__ = 'lowikchanussot'


def solve(line) :
    N = int(line.strip())
    if N == 0: return 'INSOMNIA'
    seen = set()
    P = 0
    while len(seen) != 10:
        P += N
        for c in str(P):
            seen.add(c)
    return P


def solve_A(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        lines = file.readlines()
        n_cases = int(lines[0].strip())
        for case, line in enumerate(lines[1:]) :
            sol = solve(line)
            ofile.write("Case #{c}: {s}\n".format(c=case+1, s=sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '_out.txt'
    solve_A(input, output)