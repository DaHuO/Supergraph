import os, sys
import collections as coll
import functools as ft
import itertools as it

# get problem letter from script name
problem_letter = sys.argv[0].split('.')[0]
data_set = sys.argv[1]
#attempt_number = sys.argv[2]

input_filename = "%s-%s.in" % (problem_letter, data_set)
input_file = open(input_filename)
lines = [line[:-1] for line in input_file.readlines()[1:]][:]

output_filename = "%s.out" % problem_letter
output_file = open(output_filename, "w+")
sys.stdout = output_file

def get_chunks(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i:i+n]

from jamcode import *
lines_per_case = 1
chunks = get_chunks(lines, lines_per_case)

def get_answer(chunk):
    digits_needed = [0,1,2,3,4,5,6,7,8,9]
    N = int(chunk[0])
    if N == 0:
        return "INSOMNIA"
    i = 0
    while digits_needed:
        i += 1
        n = N * i
        digits_needed = set(digits_needed) - set(map(int,str(n)))
    return n


for i, chunk in enumerate(chunks):
    print "Case #%s: %s" % (i+1, get_answer(chunk))

input_file.close()
output_file.close()
