#Nick Robertson

import random
import os
import string
import math

def all_happy(array):
	count =0
	size = len(array)
	for element in array:
		if(element ==1):
			count+=1

	if (count==size):
		return 1
	return 0

def flip(array, split):
	new_array = []
	clone = []
	temp_array = array[0:split]
	
	#print "Pile Picked Up", temp_array
	for value in temp_array:
		if value ==0:
			clone.append(1)
		else:
			clone.append(0)

	clone.reverse()
	#print "Pile Flipped", clone

	new_array = clone + array[split:len(array)]
	#print "New Array", new_array
	return new_array


def sequential_swap(array):
	swap_count=0

	for i in range(len(array)-1):
		if array[i]!=array[i+1]:
			swap_count+=1
			array = flip(array,i+1)

	if  all_happy(array):
		return swap_count
	else:
		return swap_count+1

fo = open("rotp_input.txt", "rw+")
fw = open("rotp_output.txt", "w")

number_of_tests=int(fo.readline())

for i in range(number_of_tests):
	input= str(fo.readline())
	input_bin = []
	for symbol in input:
		if(symbol=='+'):
			input_bin.append(1)
		if(symbol=='-'):
			input_bin.append(0)
	flips = len(input_bin)

	if all_happy(input_bin):
		flips = 0
	else:
		flips = sequential_swap(input_bin)

	some_string = "Case #{0}: {1}\n".format(i+1, flips)
	#print some_string
	fw.write(some_string)