PROBLEM='revenge'
INPUT_DIR='./input/'
OUTPUT_DIR='./output/'

def process(item):
    """Count the number of + to - transitions in the string."""
    status = '+'
    count = 0

    for c in reversed(item):
        if c != status:
            status = c
            count += 1

    return count

def process_input(input_stream,output_stream):
    """Given an already open file object, reads the data."""
    testcases = int(input_stream.readline().strip())
    for testcase in range(testcases):
        oneline = input_stream.readline().strip()
        result = process(oneline)
        print("Case #{}: {}".format(testcase+1,result), file=output_stream)

import sys
import argparse
import fileinput

def driver():
    input_filename = INPUT_DIR + PROBLEM + '.in'
    #output_filename = OUTPUT_DIR + PROBLEM + '.out'

    parser = argparse.ArgumentParser(description='Select input and output files for contest problem')
    parser.add_argument('--input', type=str, default=input_filename,
                        help='Input filename (default={})'.format(input_filename))
    parser.add_argument('--output', type=str, default=None,
                        help='Output filename (default=stdout)')

    args = parser.parse_args()

    fin = fileinput.input(files=(args.input))
    fout = sys.stdout
    if args.output:
        fout = open(args.output,'w')

    process_input(fin, fout)

    fout.close()
    fin.close()


if __name__ == "__main__":
    driver()
