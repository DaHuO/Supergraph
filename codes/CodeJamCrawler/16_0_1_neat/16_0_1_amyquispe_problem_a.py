#!/usr/bin/env python

import fileinput

def __main__():
    first = True
    count = 1
    lines = 0
    output = ""
    for line in fileinput.input(): 
        if first:
           first = False
           lines = int(line)
           continue
        if count > lines:
           break
        else:
            if int(line) == 0: 
                output += "Case #" + str(count) + ": INSOMNIA\n"
            else:
                output += "Case #" + str(count) + ": " + str(sleeping(int(line)) ) + "\n"
            count += 1
    print output

def interesting_question():
    for i in range(1, 1000000):
        print sleeping(i)

def sleeping(num):
    largest = num
    multiplier = 1
    digit_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    while(len(digit_set) > 0):
        current = num * multiplier
        digit_set_update(digit_set, current)
        multiplier += 1
        largest = current
    return largest 

def digit_set_update(digit_set, num):
    if num == 0:
        return
    ones_digit = num % 10
    if ones_digit in digit_set:
        digit_set.remove(ones_digit)
    digit_set_update(digit_set, num / 10)

__main__()
