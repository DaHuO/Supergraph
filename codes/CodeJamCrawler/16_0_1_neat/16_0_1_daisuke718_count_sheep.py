#!/usr/bin/env python
import os
OUTPUT_FILENAME = 'output.txt'

f = open('input.txt', 'r') 
if os.path.isfile(OUTPUT_FILENAME) :
    os.remove(OUTPUT_FILENAME)
output_file = open(OUTPUT_FILENAME, 'a')

t = int(f.readline())
for a in range(t) :
    n = int(f.readline())
    i = 1
    digit_set = set()
    before_target = 0
    while len(digit_set) < 10 :
        target = n * i
        for target_s in str(target) :
            digit_set.add(target_s)
        if before_target == target :
            target = "INSOMNIA"
            break
        before_target = target
        i += 1
    output_file.write("Case #" + str(a+1) + ": " + str(target) + "\n")

