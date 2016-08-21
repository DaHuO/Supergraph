#!/usr/bin/env python

"""
Python template for Google Code Jam problems
"""

import sys
import argparse

class InputCase: # Calling this "TestCase" will make PyCharm think it's a Python unittest
    pass


def process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=argparse.FileType('r'),
                        help="Input file")
    args = parser.parse_args()

    return args

def process_input(args):
    casescount = int(args.filename.readline())
    testcases = []

    for i in range(casescount):
        casestring = args.filename.readline()

        testcase = InputCase()
        # Adjust test case variables here
        testcase.N = int(casestring)
        # secondline = args.filename.readline()
        # testcase.vs = map(int, secondline.split())
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t):
    zero_to_nine = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    n = t.N
    c = 1

    while c < 1000:

        digits = str(c * n)

        for d in digits:
            if int(d) in zero_to_nine:
                zero_to_nine.remove(int(d))

        if len(zero_to_nine) == 0:
            return(c * n)

        c += 1

    return "INSOMNIA"


def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print("Case #" + str(t + 1) + ": " + str(puzzle(testcases[t])))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)



