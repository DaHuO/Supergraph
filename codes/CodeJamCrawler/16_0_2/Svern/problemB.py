from __future__ import print_function
from options import parse_args
import math


def test_current(array):
    return array[0] == "+" and len(set(array)) == 1

def get_n_sets(array):
    n = 1
    k = 0
    i = 1
    while i < len(array):
        if array[i] == array[k]:
            i += 1
        else:
            n += 1
            k = i
            i += 1
    return n

if __name__ == "__main__":
    args = parse_args()
    infile = open(args.data_file, 'r')
    outfile = open(args.out_file, 'w')
    n = int(infile.readline())
    op = {"+":"-", "-":"+"}
    for c in xrange(n):
        string = infile.readline().strip()
        n_sets = get_n_sets(string)
        last = string[len(string)-1]
        if last == "+":
            n_sets -= 1

        outfile.write('Case #{x}: {y}\n'.format(x=c+1, y=n_sets))
