import argparse

from joblib import Parallel, delayed
import numpy as np

def flippin(stack, index):
    flips = 0
    i = stack.shape[0] - 1
    while not stack.all() == True:
        # Find the highest-index False.
        i = np.where(stack == False)[0][-1]
        stack = ~stack[:(i + 1)]
        flips += 1
    return [index, flips]

def pancake_ize(s):
    pancakes = []
    for c in list(s):
        if c == '+':
            pancakes.append(True)
        else:
            pancakes.append(False)
    return np.array(pancakes, dtype = np.bool)

def readfile(f):
    with open(f, "r") as infile:
        num = infile.readline()
        pancakes = [pancake_ize(line.strip()) for line in infile.readlines()]
    return [int(num), pancakes]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'CodeJam 2016, Problem B',
        add_help = 'How to use', prog = 'python B.py <args>')

    # Inputs.
    parser.add_argument("-i", "--input", required = True,
        help = "Input file containing the matrix S.")
    parser.add_argument("-o", "--output", required = True,
        help = "Output file.")
    args = vars(parser.parse_args())

    T, pancakes = readfile(args['input'])

    out = Parallel(n_jobs = -1, verbose = 10)(
        delayed(flippin)(pancakes[i - 1], i) for i in range(1, T + 1))
    f = open(args['output'], "w")
    for jobid, flips in sorted(out):
        s = "Case #{}: {}".format(jobid, flips)
        print(s)
        f.write("{}\n".format(s))
    f.close()
