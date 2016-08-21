#!/usr/bin/env python

def findFirst(stack, mood):
	for i in range(0,len(stack)):
		if stack[i] == mood:
			return i
	return -1 # all mood

def findFirst(mood, stack, start, end):
	for i in range(start, end):
		if stack[i] == mood:
			return i
	return len(stack)

def flip(mood, stack, start, end):
	for i in range(start, end):
		stack[i] = mood

def makeHappy(stack):
	num = 0
	size = len(stack)
	while findFirst(False, stack, 0, size) != size:
		if size == 1:
			if stack[0] != True:
				stack[0] = True
				num = num + 1
		else: 
			# more than 1 pancake not all happy
			if stack[0] == True: # start happy
				start = findFirst(False, stack, 0, size)
				flip(False, stack, 0, start)
				num = num + 1
				# print stack, num
			else: # starts unhappy
				end = findFirst(True, stack, 0, size)
				flip(True, stack, 0, end)
				num = num + 1
				# print stack, num
	# print num
	return num


def main():
	output = []
	biglist = readInput("B-large.in")
	# biglist = [[False], [False, True], [True, False], [True, True, True], [False, False, True, False]]
	# biglist = [[False, True, False, False, False], [True, True, True, False, True, True], [False, False, False, True, False, False]]
	for stack in biglist:
		# print "...flipping", stack
		output.append(makeHappy(stack))
	print output
	writeOutput(output, "B_large.out")

def readInput(filename):
	biglist=[]
 	with open(filename) as file:
 		next(file)
 		for line in file:
 			l=[]
 			line = line.strip()
 			for c in line:
 				if c == '+':
 					l.append(True)
 				else:
 					l.append(False)
 			biglist.append(l)
 	return biglist

def writeOutput(output, filename):
	file = open(filename, "w")
	for i in range(0,len(output)):
		file.write("Case #%d: %s\n" % (i+1, output[i]))
	file.close()

if __name__ == "__main__":
    main()