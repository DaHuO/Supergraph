"""The infinite house of pancakes has just introduced a new kind of pancake! it
has a happy face made of chocolate chips on one side (the happy side) and
nothing on the other side (the blank side). 

You are the head waiter on duty, and the kitchen has just iven you a stack of
pancakes to serve to a customer. Like any good pancake server, you have X-ray
pancake vision, and you can see whether each pancake in the stack has the happy
side up or the blank side up. You think the customer will be happiest if every
pancake is happy side up when you serve them. 

You know the following maneuver: carefully lift up some number of pancakes
(possibly all of them) from the top of the stack, flip that entire group over,
and then put the group back down on top of any pancakes that you did not lift
up. When flipping a group of pancakes, you flip over the entire group in one
motion, you do NOT flip individually. Formally: if we number the pancakes 1,2,
..., N from top to bottom, you choose the top i pancakes to flip. Then, after
the flip, the stack is i, i-1, ..., 2, 1, i+1, i+2,... N. Pancakes 1,2,...,i now
have the opposite side up as they had before. 

For example, let's denote the happy side as + and the blank side as -. Suppose
that the stack, starting from the top is --+-. One valid way to execute the
maneuver would be to pick up the top three, flip the entire group, and put them
back down on the remaining fourth pancake which would remain unchanged. The new
state of the stack would be -++-. The other valid ways would be to pick up and
flip the top one, the top two, or all four. It would not be valid to choose and
flip the middle two or bottom one, because you must flip the top. 

You will not serve the customer until every pancake is happy side up, but you don't want
the pancakes to get cold, so you have to act fast! What is the smallest number
of times you will need to execute the maneuver to get all the pancakes happy
side up, if you make the optimal choice?

Input:
    The first line of input gives the number of test cases, T. T test cases
    follow. Each consists of one line with a string S, each character of which
    is either (which represents a pancake that is initially happy side up) or -
    (which represents a pancake that is initially blank side up). The string,
    when left to right, represents the stack as when viewed from top to bottom.

Output:
    For each test case, output one line containing Case# x: y, where x is the
    test case number (starting from 1) and y is the minimum number of times you
    will need to execute the maneuver to get all the pancakes happy side up."""

# notes
# maximum index of 1 or 0 via enumerate                    i
# replace all + with 1 and all - with 0
# map(int(list(input_string.replace(('+','1').replace('-','0')
#
cases = int(input())
case = 1
for i in range(cases):
    flips = 0
    stack = list(str(input()))
    while stack:
        if stack[-1] == '+':
            stack.pop()
            continue
        else:
            for i, cake in enumerate(stack):
                if cake == '+':
                    stack[i] = '-'
                if cake == '-':
                    stack[i] = '+'
        flips += 1
    print(("Case #%d: " + str(flips)) % case)
    case += 1
