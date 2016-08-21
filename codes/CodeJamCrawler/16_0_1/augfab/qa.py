#!/usr/bin/env python

import sys

def get_last(n):
    digits = {str(i): 0 for i in range(10)}
    current_n = n
    if n == 0:
        return "INSOMNIA"
    while 0 in digits.values():
        current_n_str = str(current_n)
        for d in range(len(current_n_str)):
            digits[current_n_str[d]] += 1
        current_n += n
    return str(current_n - n)

def main():
    fh = open(sys.argv[1])
    fhout = open("out", "w")

    cases = int(fh.readline().strip())
    i = 0

    while i < cases:
        i += 1
        n = int(fh.readline().strip())
        last = get_last(n)
        fhout.write("Case #{}: {}\n".format(i, last))

    fhout.flush()
    fh.close()
    fhout.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
