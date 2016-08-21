#!/usr/bin/python

import sys

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

def check_all_numbers(l):
    for i in range(0, 10):
        if str(i) not in l:
            return False
    return True

row_number = 0
with open(in_file_name, "r") as in_file:
    with open(out_file_name, "w") as out_file:
        for line in in_file:
            found_numbers = []
            if row_number == 0:
                row_number += 1
                end_number = int(line.rstrip())
                continue
            n = int(line.rstrip())

            if n == 0:
                out_file.write("Case #" + str(row_number) + ": INSOMNIA\n")
                row_number += 1
                continue

            n_tmp = n
            i = 0
            while True:
                i += 1
                n_tmp = n * i
                for num in str(n_tmp):
                    if num not in found_numbers:
                        found_numbers.append(num)
                if check_all_numbers(found_numbers):
                    out_file.write("Case #" + str(row_number) + ": " + str(n_tmp) + "\n")
                    break

            row_number += 1
            if row_number > end_number:
                break
