import re

n = int(raw_input())

test_cases = [int(raw_input()) for i in range(1, n + 1)]

j = 1


def reached(list2):
    cheap = False
    for ele in list2:
        if ele != 1:
            return cheap
    return True


n = 1

for i in test_cases:
    j = 1
    if i == 0:
        print "Case #{}: {}".format(n, "INSOMNIA")
        n += 1
        continue
    test_number = i
    list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        # print test_number
        test_number = i * j
        for ch in str(test_number):
            list2[int(ch)] = 1
        # print list2
        # print "j is ", j
        if reached(list2):
            break
        j += 1
    print "Case #{}: {}".format(n, i * j)
    n += 1

# print test_cases
