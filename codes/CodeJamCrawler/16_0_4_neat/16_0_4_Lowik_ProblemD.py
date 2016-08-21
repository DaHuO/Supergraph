__author__ = 'lowikchanussot'


def solveD_small(line):
    K, C, S = [int(c) for c in line.strip().split()]
    if K != S:
        print("Error, K should be equal to S")
        return "IMPOSSIBLE"
    kc = K**(C-1)
    positions = [1 + i * kc for i in range(0, K)]
    return ' '.join([str(p) for p in positions])

def solve(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        lines = file.readlines()
        for case, line in enumerate(lines[1:]) :
            sol = solveD_small(line)
            ofile.write("Case #{c}: {s}\n".format(c=case+1, s=sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '_out'
    solve(input, output)