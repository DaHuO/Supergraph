# coding: utf-8

def resolve(case_counter, initial_number):
    digits = set()
    next_num = initial_number
    attempts_counter = 0
    while True:
        num_digits = len(digits)
        for digit in str(next_num):
            digits.add(digit)
        if len(digits) == 10:
            print "Case #{}: {}".format(case_counter, next_num)
            return
        if len(digits) == num_digits:
            attempts_counter += 1
            if attempts_counter == 100:
                print "Case #{}: {}".format(case_counter, "INSOMNIA")
                return
        else:
            attempts_counter = 0
        next_num += initial_number

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    initial = int(raw_input())
    resolve(i, initial)
