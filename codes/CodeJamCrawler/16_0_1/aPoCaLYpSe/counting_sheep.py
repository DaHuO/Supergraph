import copy
import sys


def parse_case(instrm):
    return int(instrm.readline().strip())


def solve_case(N):

    if N == 0:
        return "INSOMNIA"
    
    seen = set()
    i = 0
    while len(seen) < 10:
        i += 1
        digits = str(N*i)
        for d in digits:
            seen.add(d)
        if len(seen) == 10:
            return digits        


if __name__ == "__main__":
    instrm = open(sys.argv[1])
    ncases = int(instrm.readline().strip())
    for i in range(ncases):
        case = parse_case(instrm)
        ans = solve_case(case)
        print("Case #{}: {}".format(i+1, ans))
