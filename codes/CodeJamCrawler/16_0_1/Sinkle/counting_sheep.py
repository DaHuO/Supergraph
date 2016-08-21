#!/usr/bin/python

import sys

def count_num(n):
    digits = set()
    nums = set()
    i = 1
    while True:
        tmp = i * n
        if tmp in nums:
            return "INSOMNIA"
        nums.add(tmp)
        for c in str(tmp):
            digits.add(c)
        if len(digits) == 10:
            return str(tmp)
        i += 1

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r") as input, open(output_file, "w") as output:
        t = int(input.readline())
        for i in range(1, t + 1):
            case = int(input.readline())        
            output.write("Case #{}: {}\n".format(i, count_num(case)))

if __name__ == "__main__":
    main()
