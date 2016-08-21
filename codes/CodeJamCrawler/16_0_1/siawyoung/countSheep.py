#!/usr/bin/env python

def countsheep(num):

    original_num = num
    curr = num
    nums = set(['.', '-'])

    if num == 0:
        return 'INSOMNIA'

    while True:
        nums.update(list(str(curr)))
        if len(nums) >= 12:
            return curr
        curr += original_num

t = int(input())
for i in range(1, t + 1):
    inp = int(input())
    print("Case #{}: {}".format(i, countsheep(inp)))