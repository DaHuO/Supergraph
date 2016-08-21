import copy
import sys
import math


def parse_case(instrm):
    return [int(i) for i in instrm.readline().strip().split()]


def solve_case(case):
    K, C, S = case
    return " ".join(str(i) for i in range(1, K+1))

if __name__ == "__main__":
    instrm = open(sys.argv[1])
    ncases = int(instrm.readline().strip())
    for i in range(ncases):
        case = parse_case(instrm)
        ans = solve_case(case)
        print("Case #{}: {}".format(i+1, ans))
