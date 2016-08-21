#!/usr/bin/python

# Input   Output

# 5
# 0       Case #1: INSOMNIA
# 1       Case #2: 10
# 2       Case #3: 90
# 11      Case #4: 110
# 1692    Case #5: 5076


def is_finished(l):
    if not l[0]:
        return False

    return l.count(l[0]) == len(l)


def find_last_sheep_counted(starting_number):
    named_numbers = [False for _ in range(10)]

    i = 1

    while(not is_finished(named_numbers)):
        current_number = starting_number * i

        chars = list(str(current_number))

        if chars == list(str(starting_number * (i-1))):
            break

        for c in chars:
            named_numbers[int(c)] = True

        i += 1

    if i == 1:
        return "INSOMNIA"
    else:
        return starting_number * (i-1)

# print(0, find_last_sheep_counted(0))
# print(1, find_last_sheep_counted(1))
# print(2, find_last_sheep_counted(2))
# print(11, find_last_sheep_counted(11))
# print(1692, find_last_sheep_counted(1692))

file_name = "A-large.in"

with open(file_name, "r") as f:
    lines = f.readlines()

    for i, starting_number in enumerate(lines[1:]):
        print("Case #{}: {}".format(i+1, find_last_sheep_counted(int(starting_number))))
