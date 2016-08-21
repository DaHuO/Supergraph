

def solve(n):
    n = int(n)
    if n == 0:
        return "INSOMNIA"
    all_digits = ["1","2","3","4","5","6","7","8","9","0"]
    for k in range(1,202):
        if k == 201:
            return "INSOMNIA"
        x = int(n*k)
        # if list gets empty
        if all_digits:
            all_digits=[item for item in all_digits if item not in list(str(x))]
        else:
            return x-n



                # check out .format's specification for more formatting options
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    n = raw_input().split(" ")[0]  # read a list of integers, 2 in this case
    # for each first, second, third digits of number..
    result=solve(n)
    print "Case #{}: {}".format(i, result)
