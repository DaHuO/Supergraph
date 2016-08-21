from math import pow

count_map = {}


def count_char(line):
    for number in line.split(' '):

        count_map.setdefault(number, 0)
        count_map[number] = count_map[number] + 1

if __name__ == "__main__":
    import fileinput
    f = fileinput.input("D:/B-large.in")

    T = int(f.readline())
    for case in xrange(1, T+1):
        N = f.readline().replace("\n", "")
        N = int(N)
        count_map = {}
        for i in xrange(0, 2*N - 1):
            line = f.readline().replace("\n", "")
            count_char(line)
        res = []
        for key, value in count_map.iteritems():
            if value % 2 != 0:
                res.append(key)
        print "Case #{}: {}".format(case, ' '.join(sorted(res, key=lambda x:int(x))))

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    # t = int(raw_input())  # read a line with a single integer
    # for i in xrange(1, t + 1):
    #     # read N
    #     N = raw_input()  # read a list of integers, 2 in this case
    #     N = int(N)
    #     for i in xrange(0, 2*N - 1):
    #         line = raw_input()
    #         count_char(line)
    #     res = []
    #     for key, value in count_map.iteritems():
    #         if value % 2 != 0:
    #             res.append(key)
    #     print sorted(res)
        # print "Case #{}: {}".format(i, res)

