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
        listofcases.append(int(i[x+1][:-1]))
    print(listofcases)
    return listofcases

def solve_case(case):
    digits = set()
    number = 0
    if case == 0:
        return 'INSOMNIA'
    while digits != set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        number = number + case
        digits = digits | set(str(number))
        print(number)
        print(digits)
    return number
                            
def main(input):
    listofcases = read_input(input)
    f = open('C:\\Users\\Josh\\Documents\\Python\\output.txt', 'w')
    for x in range(len(listofcases)):
        string = 'Case #' + str(x+1) + ': ' + str(solve_case(listofcases[x])) + '\n'
        f.write(string)

main('C:\\Users\\Josh\\Documents\\Python\\A-large.in')
