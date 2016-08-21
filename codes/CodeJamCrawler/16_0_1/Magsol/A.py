import argparse
import sys

from joblib import Parallel, delayed
import numpy as np

def count_sheep(N, index):
    observed = np.zeros(10, dtype = np.int)
    iterations = 0
    if N == 0:
        return [index, 'INSOMNIA']
    new_N = N
    while np.any(observed == 0) and iterations < sys.maxsize:
        # Update the number of iterations and perform another one.
        iterations += 1
        new_N = N * iterations
        digits = map(int, list(str(new_N)))
        for d in digits:
            if observed[d] == 0:
                observed[d] = 1
    if np.any(observed == 0):
        new_N = 'INSOMNIA'
    return [index, new_N]

def readfile(f):
    num = -1
    with open(f, "r") as infile:
        num = int(infile.readline())
        Ns = [int(line.strip()) for line in infile.readlines()]
    return [num, Ns]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'CodeJam 2016, Problem A',
        add_help = 'How to use', prog = 'python A.py <args>')

    # Inputs.
    parser.add_argument("-i", "--input", required = True,
        help = "Input file containing the matrix S.")
    parser.add_argument("-o", "--output", required = True,
        help = "Output file.")
    args = vars(parser.parse_args())

    T, Ns = readfile(args['input'])

    out = Parallel(n_jobs = -1, verbose = 10)(
        delayed(count_sheep)(Ns[i - 1], i) for i in range(1, T + 1))
    f = open(args['output'], "w")
    for jobid, counts in sorted(out):
        s = "Case #{}: {}".format(jobid, counts)
        print(s)
        f.write("{}\n".format(s))
    f.close()
