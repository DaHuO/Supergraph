#!/usr/bin/python

import math


def solve(n):
    nums = set()
    for i in range(1, 1000001):
        result = i * n
        for num in str(result):
            nums.add(num)
        if len(nums) == 10: return result
    return 'INSOMNIA'

if __name__=='__main__':
    input_file = open("input.in")
    output_file = open("output.out", 'w')
    test_cases = int(input_file.readline().strip())

    # Loop through all test cases
    for test_case_number in range(1, test_cases+1):
        n = int(input_file.readline().strip())
        string = 'Case #%s: %s' % (test_case_number, solve(n))
        print string
        output_file.write(string + '\n')
    input_file.close()
    output_file.close()