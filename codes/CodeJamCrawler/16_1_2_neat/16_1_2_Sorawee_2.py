import sys    
from itertools import groupby

def solve(rows):
    for k, v in groupby(sorted(rows)):
        if len(list(v)) % 2 == 1:
            yield str(k)

def main():
    nums = map(int, sys.stdin.read().split())
    t = next(nums)
    for case in range(1, t + 1):
        n = next(nums)
        rows = [next(nums) for j in range(n*(2*n-1))]
        print('Case #{}: {}'.format(case, ' '.join(solve(rows))))
    
main()