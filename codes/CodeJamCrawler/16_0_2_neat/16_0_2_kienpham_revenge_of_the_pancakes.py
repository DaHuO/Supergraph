#!/usr/bin/env python3
import sys
from code_jam import CodeJam

def solve(i, data):
    tries = 0
    while True:
        # print("tries: ", tries)
        # print("data: ", data)

        for k, v in enumerate(data):
            if '-' not in data:
                return tries
            elif '+' not in data:
                return tries+1

            try:
                # print(data[k], data[k+1])

                if data[k] != data[k+1]:
                    # flip all previous:
                    previous_index = 0
                    while k - previous_index >= 0:
                        data[previous_index] = data[k+1]
                        previous_index += 1
                    # print('data after flip ', data)
                    tries += 1
                    break
            except IndexError:
                return tries

        # exit()
    # cj.print_output(i, 2)
    # exit()

if __name__ == "__main__":
    cj = CodeJam(sys.argv)
    test_cases, data = cj.run()

    for i in range(0, test_cases):
        tries = solve(i, [x for x in data[i]])
        cj.print_output(i+1, tries)
        # exit()
