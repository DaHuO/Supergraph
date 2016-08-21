f = open('b.out', 'w')
n = input()
for i in range(0, n):
    f.write('Case #' + str(i + 1) + ': ')
    line = raw_input()
    a = []
    for i in range(0, len(line)):
        if line[i] == '+':
            a += [1]
        else:
            a += [0]

    a = a[::-1]
    flag = 1
    count = 0
    for i in a:
        if not i == flag:
            count += 1
            flag = i
    # count = 0
    # while (0 in a):
    #     zero_index = len(a) - a[::-1].index(0)
    #     a = a[0: zero_index]
    #     if (a[0] == 1):
    #         one_index = a.index(1)
    #         count += 1
    #         a = [1] * (one_index) + a[one_index + 1:]
    #     count += 1
    #     a = a[::-1]
    #     for i in range(0, len(a)):
    #         a[i] = 1 - a[i]
    f.write(str(count) + '\n')
    # print(count)
f.close()