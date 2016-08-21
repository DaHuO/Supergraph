
def get_num(data):
    t = int(data[0])
    data = data[1:]
    all_nums = set()
    tens = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    for i in range(t):
        if int(data[i]) == 0:
            print("Case #{}: INSOMNIA".format(i + 1))
        else:
            k = 2
            num = int(data[i])
            num_tens = set()
            new_num = num
            while True:
                # print(new_num, "->", end="")
                [num_tens.add(j) for j in data[i]]
                # print(sorted(list(num_tens)), new_num)
                if num_tens == tens:
                    print("Case #{}: {}".format(i + 1, new_num))
                    break

                new_num = k * num
                data[i] = str(new_num)
                k += 1


if __name__ == "__main__":
    # data = open("input.txt", "r").readlines()
    data = open("A-large.in", "r").readlines()
    data = [i.strip() for i in data]

    get_num(data)
