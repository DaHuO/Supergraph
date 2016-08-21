#!/usr/bin/env python2
with open("1.in",'r') as f:
	T = f.readline()
	for case, line in enumerate(f):

		nums = []
		line = line.lower()
		while ('z' in line):
			nums.append(0)
			for i in "zero": line = line.replace(i,'',1) 

		while ('w' in line):
			nums.append(2)
			for i in "two": line = line.replace(i,'',1) 

		while ('u' in line):
			nums.append(4)
			for i in "four": line = line.replace(i,'',1)

		while ('r' in line):
			nums.append(3)
			for i in "three": line = line.replace(i,'',1) 

		while ('x' in line):
			nums.append(6)
			for i in "six": line = line.replace(i,'',1)

		while ('g' in line):
			nums.append(8)
			for i in "eight": line = line.replace(i,'',1)

		while('o' in line):
			nums.append(1)
			for i in "one": line = line.replace(i,'',1)

		while('s' in line):
			nums.append(7)
			for i in "seven": line = line.replace(i,'',1)

		while('v' in line):
			nums.append(5)
			for i in "five": line = line.replace(i,'',1)

		while('i' in line):
			nums.append(9)
			for i in "nine": line = line.replace(i,'',1)

		nums.sort()

		print "Case #{}: {}".format(case+1, "".join(str(x) for x in nums))
