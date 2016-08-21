#!/usr/bin/env python

import sys
OUTFILE = "output_a_large.txt"


def find_sleep_number(N):
    if N == 0:
        return "INSOMNIA"
    else:
        digits = {char:1 for char in str(N)}
        current_num = N
        trial_num = 0
        while len(digits.keys()) < 10 and trial_num < 1000:
            trial_num += 1
            current_num = N*trial_num
            for char in str(current_num):
                if char not in digits.keys():
                    digits[char] = 1
        if trial_num != 100:
            return current_num
        else:
            return "INSOMNIA"



def main(lines_to_read):
    length_of_input = int(lines_to_read[0])
    all_numbers = [int(line) for i,line in enumerate(lines_to_read) if i]
    sleep_numbers = [find_sleep_number(num) for num in all_numbers]
    
    
    with open(OUTFILE, 'w') as outfile:
        for j in range(length_of_input):
            line_to_write = "Case #{}: {}\n".format(j+1,sleep_numbers[j])
            outfile.write(line_to_write)
            #sys.stdout.write(line_to_write)


if __name__=="__main__":
    main(sys.stdin.readlines())
