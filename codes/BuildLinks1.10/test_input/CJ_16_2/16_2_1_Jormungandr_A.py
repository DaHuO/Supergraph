#!/usr/bin/env python

def input_1(a):
    """(input_):
        function to parse code jam input assumes 1 line per case
        :param a: the input file string
    """

    with open(a, 'r') as input:
        num_cases = input.readline()
        cases = input.readlines()


    return num_cases, cases

def output_(a, b):
    """(output_):
        function to write output file
        :param a: list of output cases
        :param b: name of output file
    """

    i = 1
    with open(b, 'w') as output:
        for item in a:
            output.write('Case #{}: '.format(i) + str(item) + '\n')
            i +=1

def test(case):
    if ('Z' in case and 'E' in case and 'R' in case and 'O' in case):
        case.remove('Z')
        case.remove('E')
        case.remove('R')
        case.remove('O')
        number = '0'
    elif ('T' in case and 'W' in case and 'O' in case):
        case.remove('T')
        case.remove('W')
        case.remove('O')
        number = '2'
    elif ('F' in case and 'O' in case and 'U' in case and 'R' in case):
        case.remove('F')
        case.remove('O')
        case.remove('U')
        case.remove('R')
        number = '4'
    elif ('E' in case and 'I' in case and 'G' in case and 'H' in case and 'T' in case):
        case.remove('E')
        case.remove('I')
        case.remove('G')
        case.remove('H')
        case.remove('T')
        number = '8'
    elif ('T' in case and 'H' in case and 'R' in case and case.count('E') >= 2):
        case.remove('T')
        case.remove('H')
        case.remove('R')
        case.remove('E')
        case.remove('E')
        number = '3'
    elif ('S' in case and 'I' in case and 'X' in case):
        case.remove('S')
        case.remove('I')
        case.remove('X')
        number = '6'
    elif ('F' in case and 'I' in case and 'V' in case and 'E' in case):
        case.remove('F')
        case.remove('I')
        case.remove('V')
        case.remove('E')
        number = '5'
    elif ('S' in case and 'V' in case and 'N' in case and case.count('E') >= 2):
        case.remove('S')
        case.remove('E')
        case.remove('V')
        case.remove('E')
        case.remove('N')
        number = '7'
    elif ('O' in case and 'N' in case and 'E' in case):
        case.remove('O')
        case.remove('N')
        case.remove('E')
        number = '1'
    elif ('I' in case and 'E' in case and case.count('N') >= 2):
        case.remove('N')
        case.remove('I')
        case.remove('N')
        case.remove('E')
        number = '9'
    return number, case


num_cases, cases = input_1('A-large.in')

Results = []


for case in cases:
    number = []
    case = case.strip('\n')
    case = list(case)
    while len(case) > 0:
        tmp, case = test(case)
        number.append(tmp)
    number.sort()
    Results.append(''.join(number))

output_(Results, 'A-large.out')
