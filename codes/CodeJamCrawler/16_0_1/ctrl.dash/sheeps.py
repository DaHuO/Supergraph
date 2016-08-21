
import numpy as np
import time
all_nums = set("1234567890")


def sleep_number(chosen_number):
    cur_nums = set(str(chosen_number))
    if chosen_number == 0:
        return "INSOMNIA"
    else:
        asleep = False
        i = 0
        while not asleep:
            i += 1
            res = chosen_number * i
            cur_nums.update(set(str(res)))
            if cur_nums == all_nums:
                asleep = True
                return res


with open("A-large.in") as infile:
    with open("sheeps-large.out", "w+") as outfile:
        num_cases = int(infile.readline())

        for row in range(1, num_cases + 1):
            chosen_number = int(infile.readline().strip())
            res = sleep_number(chosen_number)
            start = time.time()
            print(chosen_number, res, (time.time() - start) % 60)
            outfile.write("Case #{0}: {1}\n".format(row, res))
