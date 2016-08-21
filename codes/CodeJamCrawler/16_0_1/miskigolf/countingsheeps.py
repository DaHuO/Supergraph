#!/usr/bin/env python
import sys, os.path 

PROBLEM_ID = "A" # A B or C
PROBLEM_SIZE = "small"

file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
in_f = open('{}.in'.format(file_name), 'r')
rl = in_f.readline

testcases = rl()
#line = rl()
n = 1
#(N, L)  =  line.split(" ")

while n <= int(testcases):
    N = int(rl().rstrip())
    digits = {}
    count = 0
    nr = N
    while len(digits) < 10 and nr != 0:
        nr = N * (count + 1)
        nrstr = str(nr)
        while len(nrstr) > 0:
            digits[nrstr[0]] = 1
            nrstr = nrstr[1:]
        count = count + 1
  
    if nr != 0:
        answer = str(nr)
    else:
        answer = "INSOMNIA"
        
    print "Case #" + str(n) + ": " + answer
    n = n + 1



