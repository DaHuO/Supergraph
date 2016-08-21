##input = open('D-sample-input.txt', 'r')
##output = open('D-sample-output.txt', 'w')

input = open('D-small-attempt0.in', 'r')
output = open('D-small.out', 'w')

##input = open('D-large.in', 'r')
##output = open('D-large.out', 'w')

from math import sqrt
import random

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(k, c, s):
    return " ".join([str(x) for x in range(1, k+1)])              

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        k, c, s = read_ints()
##        if case == 1:
        solution = solve(k, c, s)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
