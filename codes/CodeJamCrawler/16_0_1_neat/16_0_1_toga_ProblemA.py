#!/bin/env python3
"""
"""
import os
import sys


def main():
    input_file = sys.argv[1]
    output_file = "./result-{0}".format(os.path.basename(input_file))
    case_T = 0
    case_num = 1
    result = ""
    with open(input_file, "r") as in_f, open(output_file, "w") as f:
        for line in in_f:
            if case_T == 0:
                case_T = int(line)
                print(case_T)
            else:
                N = str(line.strip())
                tmp = [False] * 10
                result = ""
                count = 0
                print(N)

                if N == str(0):
                    print("INSOMNIA")
                    result = "INSOMNIA"
                else:
                    while True:
                        count += 1
                        print(result, count)
                        result = str(int(N) * count)

                        for i in range(10):
                            if str(i) in result:
                                tmp[i] = True

                        if False not in tmp:
                            break

                f.write("Case #{0}: {1}\n".format(case_num, result))
                case_num += 1

if __name__ == "__main__":
    main()
