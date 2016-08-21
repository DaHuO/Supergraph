from __future__ import print_function
#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = 0

def sort(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[0]
		for x in array:
			if x[0] < pivot[0]:
				less.append(x)
			if x[0] == pivot[0]:
				equal.append(x)
			if x[0] > pivot[0]:
				greater.append(x)
		return sort(less)+equal+sort(greater)

	else:
		return array

def compute_diff_list(array):
	dict = {}
	for list_i in array:
		for num in list_i:
			#print str(num)
			if num in dict:
				dict[num] += 1
			else:
				dict[num] = 1

	result = []
	for key in dict:
		if(dict[key]%2 != 0):
			result.append(key)

	sorted(result)
	return result



def find_missing_list(array):
	dict = {}

	for list_i in array:
		for num in list_i:
			if num in dict:
				dict[num] += 1
			else:
				dict[num] = 1
	result = []

	for key in dict:
		if(dict[key]%2 != 0):
			result.append(int(key))

	result.sort()
	# sorted(result)

	return result

	# global N
	#
	# array = sort(array)
	# #print array
	#
	# diff_array = []
	# arr_length = len(array)
	# count = 0
	# while (count < arr_length-1):
	# 	if (array[count][0] != array[count+1][0]):
	# 		# print "Different!"
	# 		# print array[count]
	# 		diff_array.append(array[count])
	# 		count+=1
	# 	else:
	# 		for j in xrange(0, N):
	# 			if (array[count][j] != array[count+1][j]):
	# 				diff_array.append(array[count])
	# 				diff_array.append(array[count+1])
	# 		count += 2
	# if (count == arr_length-1):
	# 	diff_array.append(array[count])
	#
	#
	# #print diff_array
	#
	# result = compute_diff_list(diff_array)


if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		N = int(input())
		solider_list = []

		for j in xrange(0, N*2-1):
			list_input = raw_input()
			list_input = [int(i) for i in list_input.split()]
			#print list_input
			solider_list.append(list_input)

		#print solider_list
		# print("N: %i" % (N))

		print("Case #%i: " % (caseNr), end="")
		# print("Case #%i: " % (caseNr))


		result = find_missing_list(solider_list)
		# print result

		for resNr in xrange(0, N):
			print("%s " % str(result[resNr]), end="")
		print("\n", end="")