from math import sqrt; from itertools import count, islice


def get_divisor(n):
    if n % 2 == 0:
        return 2
    # for i in range(3, int(sqrt(n)) + 1, 2):
    for i in range(3, 1000, 2):
        if n % i == 0:
            return i
    return -1   # prime number


def next_number(current, length):
    global found_nums
    global limit

    if found_nums >= limit:
        return
    if length == 0:
        num = '1' + current + '1'
        # print(num)
        nbase_num_list = []
        nbase_num_divisor_list = []
        for i in range(2, 11):
            nbase_num = int(num, i)
            nbase_num_list.append(nbase_num)

        print(nbase_num_list)

        for i in nbase_num_list:
            nbase_num = i
            # print(nbase_num)
            divisor = get_divisor(nbase_num)
            # print(divisor)
            if divisor == -1:
                return
            else:
                nbase_num_divisor_list.append(str(divisor))
        # is all prime
        # print("%s %s" % (num, nbase_num_list));
        print("%s %s" % (num, " ".join(nbase_num_divisor_list)))
        f.write("%s %s\n" % (num, " ".join(nbase_num_divisor_list)))
        found_nums += 1
        return

    next_number(current + '0', length - 1)
    next_number(current + '1', length - 1)

def find_jamcoin(length):
    next_number('', length - 2)

def test():
    global found_nums
    global limit

    print("start test")
    test_cases = [[6, 3]]
    for test_case in test_cases:
        found_nums = 0
        limit = test_case[1]
        find_jamcoin(test_case[0])
        print("pass")
#test()


f = open('output.txt', 'w')

t = int(input())

for i in range(t):
    global found_nums
    global limit

    in_numbers = [int(x) for x in input().split(' ')]
    N = in_numbers[0]
    J = in_numbers[1]

    found_nums = 0
    limit = J
    print("Case #%d:" % (i + 1))
    f.write("Case #%d:\n" % (i + 1))

    jamcoins = find_jamcoin(N)
    # for j in jamcoins:
    #     print(j[0] + " " + " ".join(j[1]))

