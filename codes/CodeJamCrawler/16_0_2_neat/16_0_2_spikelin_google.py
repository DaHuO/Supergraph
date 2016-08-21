# __author__ = 'xjlin'
# -*- coding: utf-8 -*-

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())# read a line with a single integer
def flip(pancake):
    time = 0
    temp = 0
    for j in range(len(pancake)- 1):
            n = pancake[j]
            m = pancake[j+1]
            if n == m:
                pass
            elif n =='-':
                time += 1
                pancake[j] = '+'
            elif n == '+':
                time += 2
                for k in range(j+1, len(pancake)):
                    if pancake[k] == '-':
                        pancake[k] = '+'
                    else:
                        break
    if len(pancake) == 1:
        if pancake[0] == '-':
            time = 1
    for j in range(len(pancake)):
        if pancake[j] == '-':
            temp += 1
    if temp == len(pancake):
        time = 1
    return time
for i in range(1, t + 1):
    pancake = input()
    pancake = list(pancake)
    #print(type(pancake))
    time = flip(pancake)
    #print(time)
    print("Case #{}: {}".format(i, time))
    # check out .format's specification for more formatting options