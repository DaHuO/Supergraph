def count_sheep(n):
    if n == 0:
        return -1

    count = 0
    while True:
        count += 1
        multiple_n = n * count
        for j in str(multiple_n):
            digits[int(j)] = True

        # print(multiple_n)
        # print(digits)

        if False in digits:
            continue
        else:
            return multiple_n


t = int(input())

for i in range(t):
    digits = [False] * 10
    n = int(input())

    multiple_n = count_sheep(n)
    if multiple_n == -1:
        print("Case #%d: %s" % (i + 1, "INSOMNIA"))
    else:
        print("Case #%d: %d" % (i + 1, multiple_n))


