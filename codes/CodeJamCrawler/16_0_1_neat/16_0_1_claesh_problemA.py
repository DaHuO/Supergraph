#
# problemA.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

# Parser
def parser(fin):
    N = fin.readInt()
    return N

# Solver
def solver(data):
    N = data

    if N == 0:
        return 'INSOMNIA'

    i = 0
    digits = set()
    while len(digits) != 10:
        i += 1
        digits |= set(list(str(N*i)))

    return i*N


# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
