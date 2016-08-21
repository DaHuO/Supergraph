'''run in same directory as input file'''
import sys
from os.path import splitext

infile_name = sys.argv[1]
infile = open(infile_name)
outfile = open('solve_{}.txt'.format(splitext(infile_name)[0]), 'w')

INS = 'INSOMNIA'


def write_solution(case_nr, solution):
    outfile.write('Case #{}: {}\n'.format(i, solution))

count = int(infile.readline())

for i, case in enumerate(range(count), 1):
    n = int(infile.readline())

    if n == 0:
        write_solution(i, INS)
        continue

    seen = set()
    for j in xrange(1, 100):
        product = n * j
        seen.update(str(product))
        if len(seen) == 10:
            print '{} => {}'.format(n, j)
            write_solution(i, product)
            break
    else:
        raise Exception('No solution for number: {}'.format(n))
