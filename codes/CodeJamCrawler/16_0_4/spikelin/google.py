# __author__ = 'xjlin'
# -*- coding: utf-8 -*-


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())# read a line with a single integer

for i in range(1, t + 1):
    #n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    k, c, s = [int(s) for s in input().split(" ")]
    print("Case #{}:".format(i),end='')
    for j in range(1, s+1):
        print(' '+ str(j),end='')
    print('\n')

    #print("Case #{}: {}".format(i, n))
    # check out .format's specification for more formatting options