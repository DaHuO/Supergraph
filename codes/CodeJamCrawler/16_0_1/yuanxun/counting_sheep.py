def count_sheep(init_n):
    digits = []
    count = 2
    num = init_n
    while True:
        digit = map(int, str(num))
        digits += digit
        if len(set(digits)) == 10:
            return num
        else:
            num = count * init_n
            if num == init_n:
                return "INSOMNIA"
            count += 1

if __name__ == '__main__':
    # line_num = 0
    # p_f = open('output', 'w')
    # with open('A-small-attempt1.in') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if line_num == 0:
    #             line_num += 1
    #             continue
    #         else:
    #             ret = count_sheep(int(line))
    #             result = "Case #{}: {}".format(line_num, ret)
    #             p_f.write(result + '\n')
    #             line_num += 1
    # p_f.close()
    # f.close()
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = [int(s) for s in raw_input().split(" ")][0]  # read a list of integers, 2 in this case
        ret = count_sheep(n)
        print "Case #{}: {}".format(i, ret)
