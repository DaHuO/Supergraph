#!/usr/bin/env python

__author__ = 'Bill'


def input_(a):
    """(input_):
        function to parse code jam input
        :param a: the input file string
    """

    with open(a, 'r') as input:
        num_cases = int(input.readline())
        tmp = num_cases
        N = []
        j = 0
        pagess = []
        while tmp > 0:
            N.append(int(input.readline()))
            tmp2 = 2*N[j] -1
            pages = []
            while tmp2 > 0:
                page = input.readline()
                nums = [int(page.split(' ')[i]) for i in xrange(N[j])]
                pages.append(nums)
                tmp2 -= 1
            pagess.append(pages)
            tmp -= 1
            j += 1


    return num_cases, N, pagess

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

