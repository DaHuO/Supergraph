from __future__ import print_function

import sys

try:
    input = raw_input
except NameError:
    pass

if __name__ == '__main__':
    num_cases = input()

    for case_idx, starting_num in enumerate(iter(sys.stdin.readline, ''), 1):
        starting_num = int(starting_num)

        if starting_num == 0:
            print("Case #{}: INSOMNIA".format(case_idx))
        else:
            current_num = 0
            seen_digits = set()

            while len(seen_digits) != 10:
                current_num += starting_num
                current_num_digits = set(str(current_num))
                seen_digits.update(current_num_digits)
            else:
                print("Case #{}: {}".format(case_idx, current_num))
