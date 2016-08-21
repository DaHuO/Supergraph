#This file is for Problem 1 in the Qualification Round Google Code Jam 2016
#Written by Chuqiao Ren
#All rights reserved

def count(n):
    if n == 0:
        return "INSOMNIA"
    # map = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
    digits = set([])
    i = 1
    while len(digits) < 10:
        digits.update(set([int(char) for char in str(n*i)]))
        i += 1
    return n*(i-1)



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [int(s) for s in raw_input().split(" ")][0] # read a list of integers, 1 in this case
  result = count(n)
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options