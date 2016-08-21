#!/usr/bin/env python3
import argparse
import math
import logging



def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        yield f.readline()


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def main():
    for n, case in enumerate(read_input(), start=1):
        logging.info(case)
        N = int(case)
        if N == 0:
            result = "INSOMNIA"

        else:
            digits = set("")
            for i in range(1,100):
                print(case, i, N * i)
                digits.update(list(str(N * i)))
                print(digits)
                if len(digits) == 10:
                    result = N*i
                    break
            #exit(-1)
        output(n, result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="google code jam qual 2016")
    parser.add_argument("inputfile", type=str, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    outfile = open(args.inputfile + ".out", "w")
    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug("Verbose debuging mode activated")
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
        main()
