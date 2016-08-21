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
    count = 0
    result = ""
    with open(input_file, "r") as in_f, open(output_file, "w") as f:
        for line in in_f:
            if case_T == 0:
                case_T = int(line)
                print(case_T)
            else:
                N = list(line.strip())
                result = ""
                count = 0
                while True:
                    print(count, N)
                    if "-" not in N:
                        result = count
                        break
                    elif "+" not in N:
                        result = count + 1
                        break
                    else:
                        if N[-1] == "+":
                            N.pop()
                        else:
                            print(N)
                            if N[0] == "-":
                                tmp = list(map(lambda x: "-" if x == "+" else "+", N))
                                N = tmp[::-1]
                            else:
                                if N[0:-2].count("-") == 0:
                                    result = count + 2
                                    break
                                else:
                                    for i, x in enumerate(N):
                                        if x == "-":
                                            N[0:i] = "-"
                                            break

                            print(N)

                            count += 1

                f.write("Case #{0}: {1}\n".format(case_num, result))
                case_num += 1

if __name__ == "__main__":
    main()
