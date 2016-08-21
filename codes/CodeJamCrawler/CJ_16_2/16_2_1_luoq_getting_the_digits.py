import sys
def run(f, infile_name):
    outfile_name = infile_name+'.out'
    with open(outfile_name, 'w') as outfile:
        for i, line in enumerate(open(infile_name)):
            line = line.rstrip()
            if i == 0:
                continue
            outfile.write('Case #{}: {}\n'.format(i, f(line)))

import numpy as np
from collections import Counter
digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def vec(x):
    y = np.zeros(26)
    for a in x:
        y[ord(a)-ord('A')] += 1
    return y

C = np.array([vec(x) for x in digits]).T
CC = C.T.dot(C)

def getting_the_digits(line):
    x = vec(line)
    y = np.linalg.solve(CC, C.T.dot(x))
    y = np.around(y).astype(int)
    res = []
    for i, a in enumerate(y):
        for _ in range(a):
            res.append(i)
    return ''.join(map(str,sorted(res)))

if __name__ == '__main__':
    infile_name = sys.argv[1]
    run(getting_the_digits, infile_name)
