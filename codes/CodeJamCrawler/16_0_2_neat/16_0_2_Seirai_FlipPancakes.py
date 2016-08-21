#!/usr/bin/python
#####################################
# FlipPancakes.py
#   Google Code Jam 2016 Contest Exercise 2!
# Seilai Zhao
#####################################

#5
#-
#-+
#+-
#+++
#--+-

t = int(input())  # read a line with a single integer

for i in range(1, t+1):
    s = str(input())
    flipIndex = 0
    count = 0
    while("-" in s):
        count += 1
        flipIndex = s.rindex("-")
        s = s[:flipIndex+1].replace("-", "*") + s[flipIndex+1:] #as a temporary placeholder
        s = s[:flipIndex+1].replace("+", "-") + s[flipIndex+1:]
        s = s[:flipIndex+1].replace("*", "+") + s[flipIndex+1:]
    print("Case #{}: {}".format(i, count))
