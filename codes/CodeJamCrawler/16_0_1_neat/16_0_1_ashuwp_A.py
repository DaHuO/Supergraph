def sheep(num):
    if num == 0:
        return "INSOMNIA"

    itr = tr = 0

    while tr != 1023:
        cnt = 0
        itr += 1
        temp = str(num * itr)

        for k in temp:
            cnt |= 1 << int(k)

        tr |= cnt

    return num * itr


if __name__ == "__main__":

    tc = int(input())

    for i in range(tc):
        n = int(input())
        print("Case #{}: {}".format(i + 1, sheep(n)))
