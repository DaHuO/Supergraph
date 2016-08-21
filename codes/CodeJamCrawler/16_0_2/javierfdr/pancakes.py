# Google Code Jam 2016
# javierfdr@gmail.com
# Revenge of the pancakes

import sys

# Find the first 1. If is the first element no flip (0), if is the i'th element then if is the first 1 found,
# it will flip just once (1) - because previous are all 0. If is not the first 1 found, then it will always
# flip twice (once for the 0's and once for the ones at the beginning that were converted into zeroes). At the
# end if we reach a 1 o a 0, we will flip twice as well. When I say to "find a 1" I mean, the next one after at
# least a 1 followed by j zeroes.

# This idea is based on the recursive version of the Revenge of the pancakes problem. Assumming 1 is happy face and 0
# is blank side, each case is represented with binary numbers. The basic idea is to look for the next
# 1 and convert the previous series (top N-i of the tower) to ones. In order to convert to ones, since
# the previous series will be X times numbers 1, then Y times numbers 0, and then the next 1 (cursor) -
# followed by the rest of the non-sorted or non-flipped series of the tower, the idea is to flip the previous
# series, and then flip the remaining 0's of the previous series

# Tower will be taken using the strings - y + (for 0's and 1's or back side and happy side)
def findNumberOfFlips(tower):
    foundFirstOne = False
    index = 0
    prev = '+'
    flipCount = 0
    for i in tower:
        if i=='+':
            if (not foundFirstOne):
                foundFirstOne = True
                if prev == '-' and not index == 0:
                    flipCount = flipCount + 1 # first one flipCount is 1. If it was the first index flip is 0
            else:
                if (prev == '-' and (not index == 0)):
                    flipCount = flipCount + 2
        elif i == '-':
            if (index == len(tower)-1):
                if (not foundFirstOne):
                    flipCount = flipCount + 1
                else :
                    flipCount = flipCount + 2 # if is the last index and not '+' but '-' flip also twice

        prev = i
        index = index+1

    return flipCount

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):
    case = 'Case #'+str(c)+': '
    tower = in_file.readline().split()[0]
    result= case+ str(findNumberOfFlips(tower))+'\n'
    out_file.write(result)