def count(n):
    n = int(n)
    num_set = set()
    i = 1
    if n == 0:
        result = "INSOMNIA"
    else:
        while len(num_set) < 10:
            temp = n*i
            str_temp = str(temp)
            for x in str_temp:
                num_set.add(int(x))
            i += 1
        result = temp
    return result


if __name__ == "__main__":
    import fileinput
    f = fileinput.input("D:/A-large.in")

    T = int(f.readline())
    for case in xrange(1, T+1):
        N = f.readline()
        res = count(N)

        print("Case #{0}: {1}".format(case, res))
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    # t = int(raw_input())  # read a line with a single integer
    # for i in xrange(1, t + 1):
    #     n = raw_input()  # read a list of integers, 2 in this case
    #     res = count(n)
    #     print "Case #{}: {}".format(i, res)
        # check out .format's specification for more formatting options