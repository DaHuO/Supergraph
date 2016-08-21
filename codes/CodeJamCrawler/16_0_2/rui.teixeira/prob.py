#!/usr/bin/python3

cases = int(input())


def answer(case, a):
    print("Case #{}: {}".format(case + 1, a))


def calc():
    pass

for case in range(cases):
    count = 0
    p_list = list(input())
    for i in range(1, len(p_list)):
        # print(i, p_list)
        if p_list[i-1] != p_list[i]:
            count += 1
    if p_list[-1] == '-':
        count += 1
    answer(case, count)




