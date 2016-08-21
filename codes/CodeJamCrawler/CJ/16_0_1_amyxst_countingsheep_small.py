t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    curr_num = input()

    if curr_num == '0':
        print("Case #{}: {}".format(i, "INSOMNIA"))

    else:
        m = 1
        digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while True:
            next_num = str(int(curr_num) * m)
            # print("Checking: {}".format(next_num))

            for d in next_num:
                if d in digit_list:
                    digit_list.remove(d)

            if not digit_list:
                print("Case #{}: {}".format(i, next_num))
                break

            m += 1