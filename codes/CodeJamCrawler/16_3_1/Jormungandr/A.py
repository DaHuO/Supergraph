#!/usr/bin/env python

def input(a):
    """(input_):
        function to parse code jam input assumes 2 line input with first line being number of elements in 2nd line
        :param a: the input file string
    """

    with open(a, 'r') as input:
        num_cases = int(input.readline())
        tmp = num_cases
        N = []
        j = 0
        senators_list = []
        while tmp > 0:
            N.append(int(input.readline()))
            senator = input.readline()
            senators = [int(senator.split(' ')[i]) for i in xrange(N[j])]
            senators_list.append(senators)
            tmp -= 1
            j += 1


    return num_cases, N, senators_list

def output_(a, b):
    """(output_):
        function to write output file
        :param a: list of output cases
        :param b: name of output file
    """

    i = 1
    with open(b, 'w') as output:
        for item in a:
            output.write('Case #{}: '.format(i) + item + '\n')
            i +=1


num_cases, cases, senators_list = input('A-small-attempt1.in')

Results = []

parties = {0:'A', 1: 'B', 2: 'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}


for senators in senators_list:
    result = ''
    total = sum(senators)
    while total > 0:
        largest = 0
        letter = 0
        for i, s in enumerate(senators):
            if (s > largest):
                largest = s
                letter = i
        senators[letter] -= 1
        result += str(parties[letter])
        if total%2 != 0:
            result += ' '
        total -= 1


    Results.append(result)



output_(Results, 'A-small.out')
