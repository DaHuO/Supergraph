def flip(pancakes):
    flag = False
    blank_count = 0
    for s in pancakes.replace('\n', ''):
        if s == "+":
            if flag is True:
                blank_count += 1
            flag = False
        else:
            flag = True

    if flag is True:
        blank_count += 1

    if blank_count == 0:
        count = 0
    elif blank_count == 1:
        count = 1
    else:
        count = (blank_count - 2) * 2 + 3

    if pancakes.startswith("+") and count > 0:
        count += 1

    return count

if __name__ == "__main__":
    import fileinput
    f = fileinput.input("D:/B-large.in")

    T = int(f.readline())
    for case in xrange(1, T+1):
        N = f.readline()
        res = flip(N)

        print("Case #{0}: {1}".format(case, res))
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    # t = int(raw_input())  # read a line with a single integer
    # for i in xrange(1, t + 1):
    #     n = raw_input()  # read a list of integers, 2 in this case
    #     res = flip(n)
    #     print "Case #{}: {}".format(i, res)
