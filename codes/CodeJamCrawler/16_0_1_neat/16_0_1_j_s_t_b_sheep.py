#!/usr/bin/env python3

MAX_ITERATIONS = 1000

import time
filename = "A-large"

with open(filename + ".in", 'r') as inputfile:
    lines = inputfile.readlines()

with open(filename + ".out", 'w') as outputfile:
    number_of_tests = 0
    for linenumber, line in enumerate(lines):
        if linenumber == 0:
            number_of_tests = int(line.strip())
            print("There are {} tests".format(number_of_tests))
        elif linenumber > number_of_tests:
            break
        else:
            casenumber = linenumber
            N = int(line.strip())
            
            digits = set()
            for i in range(1, MAX_ITERATIONS):
                number = i*N
                digits.update(str(number))
                if len(digits) == 10:
                    resulttext = "{}".format(number)
                    break
            
            if i == MAX_ITERATIONS - 1:
                resulttext = "INSOMNIA"

            answer = "Case #{}: {}\n".format(casenumber, resulttext)
            print(answer)
            outputfile.write(answer)
            
