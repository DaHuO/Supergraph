__author__ = 'lowikchanussot'


def count_swithes(t):
    if not t:
        return 0
    n_switches = 0
    previous = t[0]
    for curr in t[1:]:
        if curr != previous:
            n_switches += 1
            previous = curr
    return n_switches


def solveB(s):
    if not s: return 0
    t = [-1 if c=='-' else 1 for c in s]
    switches = count_swithes(t)
    if switches%2 == 0 and t[0] == -1:
        return switches + 1
    if switches%2 == 1 and t[0] == 1:
        return switches + 1
    return switches


def solve(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        lines = file.readlines()
        for case, line in enumerate(lines[1:]) :
            sol = solveB(line)
            ofile.write("Case #{c}: {s}\n".format(c=case+1, s=sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '_out'
    solve(input, output)