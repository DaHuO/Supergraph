'''
Created on 27 Feb 2016

@author: Josh
'''
import math
import decimal
from itertools import count

def read_input(inputfile):
    i = open(inputfile)
    i = i.readlines()
    cases = int(i[0])
    listofcases = []
    for x in range(cases):
        listofcases.append(i[x+1][:-1])
    print(listofcases)
    return listofcases

def solve_case(case):
    length = len(case)
    last = '+'
    count = 0
    for x in range(length):
        if case[-(x+1)] != last:
            count = count + 1
            last = case[-(x+1)]
    return count
                            
def main(input):
    listofcases = read_input(input)
    f = open('C:\\Users\\Josh\\Documents\\Python\\output.txt', 'w')
    for x in range(len(listofcases)):
        string = 'Case #' + str(x+1) + ': ' + str(solve_case(listofcases[x])) + '\n'
        f.write(string)

main('C:\\Users\\Josh\\Documents\\Python\\B-large.in')
print(solve_case('-'))
print(solve_case('-+'))
print(solve_case('+-'))
print(solve_case('+++'))
print(solve_case('--+-'))
