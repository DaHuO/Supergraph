#!/usr/bin/env python3
import argparse
import math
import logging
import itertools
import collections

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        yield f.readline()


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def winstring(s):

    old = collections.deque(s)
    print("old", old)
    new = collections.deque()
    new.append(old.popleft())
    print("new", new)
    while len(old) > 0:
        c = old.popleft()
        if c >= new[0]:
            new.appendleft(c)
        else:
            new.append(c)
        print(new)
    return "".join(new)


def main():
    for n, case in enumerate(read_input(), start=1):
        logging.info(case)

        S = case.strip()
        new = winstring(S)
        output(n, new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="google code jam 2016 round 1")
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
