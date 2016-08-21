#!/usr/bin/python2
from sys import argv

goal_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
def success(chars):
    return chars >= goal_set

def get_chars(N):
    return set(str(N))

def last_num(N, case):
    i = 0
    chars_so_far = set()
    while i < 99:
        if (N == 0):
            print "CASE #%s:" % case, "INSOMNIA"
            return

        i += 1
        num = i * N
        chars = get_chars(num)
        chars_so_far = chars_so_far | chars
        if success(chars_so_far):
            print "CASE #%s:" % case, num
            return


input_file = argv[1]
f = open(input_file, 'r')

nlines = int(f.readline())
for i in xrange(nlines):
    N = f.readline()
    last_num(int(N), i+1)

f.close()

