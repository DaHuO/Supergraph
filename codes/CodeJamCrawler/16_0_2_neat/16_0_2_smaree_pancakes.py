# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

    # input is the string
    stack = input()

    # We count how many groups of symbols there are.
    # the number of flips is the number of groups,
    # minus 1 if the ending group is a + group.

    stack_split_min = list(filter(bool, stack.split("-")))
    stack_split_plus = list(filter(bool, stack.split("+")))

    print("Case #{}: {}".format(i, len(stack_split_plus)+len(stack_split_min)-stack.endswith("+")))
    # check out .format's specification for more formatting options

