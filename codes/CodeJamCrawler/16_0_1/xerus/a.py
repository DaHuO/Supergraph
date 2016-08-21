#!/usr/bin/env python3

valid = set("0123456789")

def answer(N, i=1, nums=set()):
    nums.update(str(N*i))
    if nums == valid:
        nums.clear()
        return str(N*i)
    if N == 0:
        nums.clear()
        return "INSOMNIA"
    return answer(N, i + 1, nums)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    N = int(input())  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, answer(N), set()))
    # check out .format's specification for more formatting options
