#!/usr/bin/env python3
from math import sqrt

def is_composite(number):
    for i in range(2,min(1000, (int(sqrt(number))+1))):
        if number % i == 0:
            return i
    return False


num_test_cases = int(input().rstrip())

for case in range(1,num_test_cases+1):
    print("Case #{}:".format(case))
    n, j = map(int, input().rstrip().split())
    #Generates the first binary string that has length n, starts with 1, and ends with 1
    #Converts to a base-10 int
    current_binary_string = '1' + ('0' * (n - 2)) + '1'
    #and generates a list representing its value in bases [2,10]
    numbers = [int(current_binary_string, base) for base in range(2,11)]
    found_jams = 0
    while found_jams != j:
        data = list(map(is_composite,numbers))
        if all(data):
            print(numbers[-1],' '.join(map(str,data)))
            found_jams += 1
        current_binary_string = bin(int(current_binary_string, 2)+2)[2:]
        numbers = [int(current_binary_string, base) for base in range(2,11)]


