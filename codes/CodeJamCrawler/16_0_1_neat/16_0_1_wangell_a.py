#!/usr/bin/python

import sys, os

def complete_digits(n):
    pass

if __name__ == "__main__":

    first_line = True
    n_cases = 0
    cur_case = 1

    with open(sys.argv[1], "r") as f:
        for l in f:
            if first_line:
                n_cases = int(l)
                first_line = False
            else:
                n = int(l)

                if n == 0:
                    print("Case #{}: {}".format(cur_case, "INSOMNIA"))

                else:
                    i = 1
                    cur_numbers = []

                    while True:
                        for d in list(str(n*i)):
                            if d not in cur_numbers:
                                cur_numbers.append(d)
                        if len(cur_numbers) == 10:
                            break
                        i += 1
                    print("Case #{}: {}".format(cur_case, n*i))
                cur_case += 1
