#! /usr/bin/python

import sys

def last_number_until_sleep(n):
    if n == 0:
        return "INSOMNIA"
    
    current = 0
    digits = {}
    while len(digits) < 10:
        current += n
        for i in str(current):
            digits[i] = 1
    
    return current


if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    
    for test_number in range(1, num_tests + 1):
        n = int(sys.stdin.readline())
        print("Case #{}: {}".format(test_number, last_number_until_sleep(n)))