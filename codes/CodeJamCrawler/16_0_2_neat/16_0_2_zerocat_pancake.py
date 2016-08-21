#!/usr/bin/python
# coding=utf-8
import sys


def pancake(string):
	if len(string) == 0:
		return 0
	count = 0
	if string[-1] == '-':
		count = 1

	# check how many sign switch
	# string[i] != string[i+1]
	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			count += 1
	# print  string , count
	return count


file = open(sys.argv[1], 'r')
writeFile = open(str(sys.argv[2]), 'w')
T = int(file.readline())
for i in range(T):
	str = file.readline().strip('\n')
	out = pancake(str)
	writeFile.write("Case #%i: %s\n"%(i + 1, out))

file.close()
writeFile.close()
