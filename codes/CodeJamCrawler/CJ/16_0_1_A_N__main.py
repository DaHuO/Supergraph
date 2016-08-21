#! /usr/bin/env python3

import sys

if (len(sys.argv) > 1):
    input_filename = sys.argv[1]
else:
    input_filename = "input.txt"



def sol(base):
    if base == 0:
        return "INSOMNIA"

    d = {}
    for i in range(0, 10):
        d[str(i)] = False

    num_unseen = 10

    i = 1
    while (num_unseen > 0):
        n = base*i
        i+=1

        s = str(n)
        for char in s:
            if d[char] == False:
                d[char] = True
                num_unseen -= 1


    return n



with open(input_filename, 'r') as f:
    num_cases = int(f.readline())

    for i in range(num_cases):
        n = int(f.readline())
        solution = sol(n)
        print("Case #{}: {}".format(i+1, solution))
        

