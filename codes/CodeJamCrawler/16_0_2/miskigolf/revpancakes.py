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
BLANK_SIDE = "-"
HAPPY_SIDE = "+"

def flip_side( cakes ):
    flipped_cakes = cakes[::-1]
    i = 0
    flip_side_cake = ""
    while i < len(flipped_cakes):
        if flipped_cakes[i] == BLANK_SIDE:
            flip_side_cake  += HAPPY_SIDE
        else:
            flip_side_cake  += BLANK_SIDE
        i = i + 1
    
    return flip_side_cake  
        
while n <= int(testcases):
    cakes = rl().rstrip()
    # "--+-"
    manouver = 0 
    while cakes.find(BLANK_SIDE) != -1:
        # try to make all cakes
        # left to right positive 
        ri = cakes.rfind(BLANK_SIDE) 
        li = 0
        while cakes[li] == flip_side(cakes[ri]):
            ri = ri - 1
        cakes = flip_side(cakes[0:ri+1])+cakes[ri+1:]
        manouver = manouver + 1
        #print cakes
    
    answer = str(manouver)
    
    print "Case #" + str(n) + ": " + answer
    n = n + 1



