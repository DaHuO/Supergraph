__author__ = 'FalguniT'
import numpy as np
from random import randint

#input No of Test Cases
#no_of_test_cases = input()

with open("input.txt") as f:
    content = f.readlines()
no_of_test_cases = int(content[0])

#with open("output.txt","a") as f_handle:
#    f_handle.write('Output\n')

for case_t in range(1,no_of_test_cases + 1):
    #small input
    n = int(content[case_t])
    count_to_ten =[]
    i = 0

    input_value = n
    org_input_value = input_value

    for ch in str(input_value):
            if not(ch in count_to_ten):
                count_to_ten.append(ch)

    while len(count_to_ten) < 11:
        input_value = (i + 1 ) * org_input_value

        if(input_value == 0):
            input_value = "INSOMNIA"
            break

        #check input value has unique 0-9 digit value
        for ch in str(input_value):
            if not(ch in count_to_ten):
                count_to_ten.append(ch)

        #print("input ", input_value, "digits", count_to_ten)
        if len(count_to_ten) == 10:
            break
        i = i+1

    with open("output.txt","a") as f_handle:
        f_handle.write('Case #'+ str(case_t) +':  ' + str(input_value) + '\n')


