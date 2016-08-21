import copy
import sys
import math
from collections import Counter

sys.setrecursionlimit(10000)



dig = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGTH", "NINE"]
ddict = [Counter(d) for d in dig]


def parse_case(instrm):
    return Counter(instrm.readline().strip())
   
   
def solve_case(case):
    nlet = sum(i for i in case.values())
    nums = solve_rec(0, case)
    nums = sorted(nums)
    return "".join(map(str, nums))


def solve_rec(start, obs):
    if start == 10:
        return None
    
    allowed = True
    for c, v in ddict[start].items():
        if obs[c] < v:
            allowed = False
            break
    if allowed:
        newobs = obs - ddict[start]
        if sum(newobs.values()) == 0:
            return [start]
        attempt = solve_rec(start, newobs)
        if attempt is not None:
            return [start] + attempt
    return solve_rec(start+1, obs)


if __name__ == "__main__":
    instrm = open(sys.argv[1])
    ncases = int(instrm.readline().strip())
    for i in range(ncases):
        case = parse_case(instrm)
        ans = solve_case(case)
        print("Case #{}: {}".format(i+1, ans))
