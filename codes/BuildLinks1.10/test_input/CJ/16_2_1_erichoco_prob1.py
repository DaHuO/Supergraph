#!/usr/bin/python

import sys, datetime
import itertools
import string
import math
import random

# Import third-party libraries (optional)
# https://code.google.com/p/gmpy/
# import gmpy

unique = {
    'Z': 'ZERO',
    'W': 'TWO',
    'U': 'FOUR',
    'X': 'SIX'
}

sec_unique = {
    'O': 'ONE',
    'R': 'THREE',
    'F': 'FIVE',
    'G': 'EIGHT',
    'S': 'SEVEN',
}

def solve(s):
    '''
    ' Write your code here
    ' Return solution
    '''
    all_pos = {
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'N': 0,
        'O': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Z': 0
    }
    numbers = [0] * 10

    for char in s:
        try:
            all_pos[char] += 1
        except Exception, e:
            raise e

    # print all_pos
    for char in all_pos:
        n = all_pos[char]
        if all_pos[char] == 0:
            continue
        try:
            num = unique[char]
            if char == 'Z':
                numbers[0] += all_pos[char]
            elif char == 'W':
                numbers[2] += all_pos[char]
            elif char == 'U':
                numbers[4] += all_pos[char]
            elif char == 'X':
                numbers[6] += all_pos[char]
            for unique_c in num:
                # print all_pos[unique_c]
                all_pos[unique_c] -= n
                # print all_pos[unique_c]
        except Exception, e:
            continue

    # print all_pos
    for char in all_pos:
        n = all_pos[char]
        if all_pos[char] == 0:
            continue
        try:
            num = sec_unique[char]
            if char == 'O':
                numbers[1] += all_pos[char]
            elif char == 'R':
                numbers[3] += all_pos[char]
            elif char == 'F':
                numbers[5] += all_pos[char]
            elif char == 'G':
                numbers[8] += all_pos[char]
            elif char == 'S':
                numbers[7] += all_pos[char]
            for unique_c in num:
                all_pos[unique_c] -= n
        except Exception, e:
            continue

    numbers[9] = all_pos['E']

    # print all_pos

    ans = ''
    for (i, num) in enumerate(numbers):
        for n in range(num):
            ans += str(i)
    return ans
    # return 0

def main():
    # Test if at least input file is provided
    if len(sys.argv) < 2:
        print 'Please provide input file'
        print 'Usage: %s inputfile [outputfile]' % sys.argv[0]
        return
    # Start time
    timestart = datetime.datetime.now()

    # Open input and output files
    try:
        inputFile = open(sys.argv[1])
    except:
        print 'Failed to read input file %s' % sys.argv[1]
        return
    try:
        outputFile = open(sys.argv[2], 'w') if len(sys.argv) >= 3 else None
    except:
        print 'Failed to create output file %s' % sys.argv[2]
        return

    # First line of input file usually is the number of test cases.
    # Adjust if necessary
    testCases = int(inputFile.readline().strip())

    # Display number of test cases and output file name
    print '-----------------'
    print 'Test cases: %d ' % testCases
    print 'No output file' if len(sys.argv) < 3 else 'Writing to %s' % sys.argv[2]
    print '-----------------'

    # Loop through all test cases
    for testCaseNumber in range(1, testCases+1):

        '''
        ' Edit this section
        ' Read Test Case input and adjust output format
        ' Uncomment the necessary parts and adjust to your needs
        '''

        '''
        ' Integers
        '''
        # Read an integer
        # n = int(inputFile.readline().strip())


        # Read a list of integers
        # n_list = map(int, inputFile.readline().strip().split())

        # Read a matrix of integers
        #n_matrix = []
        #for i in range(n):
        #    n_matrix.append(map(int, inputFile.readline().strip().split()))

        '''
        ' Floats
        '''
        # Read a float
        #f = float(inputFile.readline().strip())

        # Read a list of flots
        #f_list = map(float, inputFile.readline().strip().split())

        '''
        ' Strings
        '''
        # Read a string
        s = inputFile.readline().strip()

        # Read a list of strings
        # s_list = inputFile.readline().strip().split()

        '''
        ' Return string.
        ' Add necessary arguments to solve() function
        ' Adjust return type if necessary (%s for string, %f for floats, etc)
        '''
        string = 'Case #%d: %s' % (testCaseNumber, solve(s))

        '''
        ' End of edit section
        '''

        # print return string and write it to output file
        print string
        if outputFile:
            outputFile.write(string + '\n')

    # Print some final info: output file name and execution time
    print '-----------------'
    print 'Written to %s' % sys.argv[2] if outputFile else 'No output file'
    print 'Elapsed time: %s' % (datetime.datetime.now() - timestart)
    print '-----------------'

    # Close input and output files
    inputFile.close()
    if outputFile:
        outputFile.close()

if __name__=='__main__':
    main()
    # test()