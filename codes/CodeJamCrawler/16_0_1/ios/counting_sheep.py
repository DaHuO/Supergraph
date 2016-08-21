#!/usr/bin/env python3

import sys

filename = sys.argv[1]
num_cases = 0

def get_nums(num, i, nums = None):
    if nums == None:
        nums = []
    for c in str(num * i):
        if not c in nums:
            nums.append(c)
    return nums

def get_last(num):
    if num == 0:
        return None, "INSOMNIA"
    elif len(get_nums(num, 1)) == 10:
        return None, str(num)
    else:
        found_nums = get_nums(num, 2)
        i = 0
        while len(found_nums) != 10:
            i = i + 1
            found_nums = get_nums(num, i, found_nums)
        return (found_nums, i * num)

with open(filename, 'r') as f:
    num_cases = int(f.readline().strip())
    print("Number of cases: %d" % (num_cases))
    for i in range(1, num_cases + 1):
        (found, last) = get_last(int(f.readline().strip()))
        print("Case #%d: %s" % (i, last))

