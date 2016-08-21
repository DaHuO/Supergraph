# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

    # input of form K C S
    K, C, S = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    # we only have to check the first K returns. So the return for each
    # input is Case #1: 1 2 3 , etc.

    print("Case #{}:".format(i), end="")

    for j in range(1,K+1):
        print(" {}".format(j), end="")
    # check out .format's specification for more formatting options

    print("")
