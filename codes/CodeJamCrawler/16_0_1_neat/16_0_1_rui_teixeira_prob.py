#!/usr/bin/python3

cases = int(input())


def answer(case, a):
    print("Case #{}: {}".format(case + 1, a))

for case in range(cases):
    digits = {}
    n = int(input())
    if n == 0:
        answer(case, 'INSOMNIA')
        continue
    i = 1
    while True:
        for each in str(n*i):
            digits[each] = 0
        # print(digits)
        if len(digits) == 10:
            answer(case, n*i)
            break
        else:
            i += 1



