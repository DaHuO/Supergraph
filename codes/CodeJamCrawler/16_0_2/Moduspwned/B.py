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
        stack = case.strip()
        flips = 0
        prev = None
        for i in reversed(stack):
            logging.debug(i)
            if prev is None:
                if i == "-":
                    flips += 1
                prev = i
                continue
            if i != prev:
                logging.debug("prev {} now {} flip".format(prev, i))
                flips += 1
            prev = i

        output(n, flips)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="google code jam 2016 qual")
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
