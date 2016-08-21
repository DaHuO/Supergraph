from string import *
import math
import numpy

def read_words(filename):
    '''
    converts a file to a list
    '''
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("in2.txt", 'r')
numcases = int(filename.readline().split()[0])

for case in range(numcases):
	number = int(filename.readline().split()[0])

	seen_digits = [0,0,0,0,0,0,0,0,0,0]
	if number !=0:
		number_copy = number

		for digit in str(number):
			seen_digits[int(digit)] = 1

		while (numpy.sum(seen_digits) < 10):
			number+=number_copy

			for digit in str(number):
				seen_digits[int(digit)] = 1

			

	if int(number) == 0:
		print "Case #" + str(case+1) + ": INSOMNIA"
	else:
		print "Case #" + str(case+1) + ":", number

