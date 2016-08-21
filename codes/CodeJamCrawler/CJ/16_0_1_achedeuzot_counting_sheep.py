#!/usr/bin/env python

import os
import sys

def main():
    with open(sys.argv[1]) as f:

        max_tests = int(f.readline())

        for i in range(0, max_tests):

            n = int(f.readline())
            if n == 0:
                print("Case #%d: INSOMNIA" % ((i + 1), ))
                continue

            # Try to solve this...
            n_initial = n
            last_seen_number = None
            seen_digits = dict()
            mult = 1
            while True:

                str_number = str(n_initial * mult)
                for digit in str_number:
                    seen_digits[digit] = True
                if len(seen_digits) == 10:
                    break
                mult += 1

            print("Case #%d: %d" % ((i + 1), (n_initial * mult)))

if __name__ == '__main__':
    main()



