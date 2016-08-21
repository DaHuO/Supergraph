#!/usr/bin/python
import sys

# Part of 2016 Google code jam

# This task finds the minimum number of pancake flips in a stack to get them all heads up
def find_min_flips(x):
    stack = []
    flips = 0

    # convert pancake stack to boolean
    for p in list(x):
        if p == '+':
            stack.append(True)
        else:
            stack.append(False)

    # skip iterations if stack is already good
    if check_stack(stack):
        return flips

    # start at the bottom pancake and work up
    for f in range(len(stack)-1,-1,-1):
        # only work on bottom pancakes than are -
        if not stack[f]:
            # go to the top of the stack
            g=0
            # flip if first pancake is -
            if not stack[g]:
                stack = flip_stack(stack,f)
                flips = flips + 1
            # if first pancake is + find how many in sequence and flip them
            # and then flip from last - on the other side
            else:
                end_seq = False

                while not end_seq:
                   if stack[g+1]:
                       g = g + 1
                   else:
                       stack = flip_stack(stack,g)
                       stack = flip_stack(stack,f)
                       flips = flips + 2
                       end_seq = True

    if not check_stack(stack):
        print 'WRONG!'
    return flips


def check_stack(stack):
    for p in stack:
        if not p:
            return False
    return True

def flip_stack(stack,i):
    before = list(stack)
    if i == 0:
        stack[0] = not stack[0]
    else:
       mid = (i+1)/2

       # accout for odd middle pancake
       if 2*((i+1)/2) != (i+1):
           stack[mid] = not stack[mid]

       # swap and flip pancakes
       for j in range(0,mid):
           stack[j], stack[i] = not stack[i], not stack[j]
           i = i - 1  

    return stack
   

T = int(raw_input().strip())

for i in range(1, T+1):
    x = str(raw_input().strip())
    result = find_min_flips(x)
    print 'Case #' + str(i) + ': ' + str(result)
