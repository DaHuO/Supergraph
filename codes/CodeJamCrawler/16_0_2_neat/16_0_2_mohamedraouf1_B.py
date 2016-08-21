#!/usr/bin/python

import math


def solve(S):
    counter = 0
    ls = list(S)
    cf = '-'
    ct = '+'
    while '-' in ls:
        change = False
        for i in range(0, len(ls)):
            if ls[i] == cf:
                ls[i] = ct
                change = True
            else:
                cf, ct = ct, cf
                break
        if change:
            counter +=1
    return counter

if __name__=='__main__':
    input_file = open("input.in")
    output_file = open("outputB.out", 'w')
    test_cases = int(input_file.readline().strip())

    # Loop through all test cases
    for test_case_number in range(1, test_cases+1):
        S = input_file.readline().strip()
        string = 'Case #%s: %s' % (test_case_number, solve(S))
        print string
        output_file.write(string + '\n')
    input_file.close()
    output_file.close()