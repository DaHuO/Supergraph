#! /usr/bin/env python

def read_value():
    return raw_input()

def count_sheep(number):
    if number is 0: return "INSOMNIA"

    digits_seen = [False] * 10

    i = 1
    while not all(digits_seen):
        last_number = i * number
        i += 1
	digits_in_last_number = list(str(last_number))
	for digit in digits_in_last_number:
	    digits_seen[int(digit)] = True

    return last_number

if __name__ == "__main__":
    TESTCASES = int(read_value())

    for i in range(TESTCASES):
        print "Case #{}: {}".format(i+1, count_sheep(int(read_value())))
