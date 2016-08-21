import sys

def main():
	testCases = input()
	# This is all you need for most Google Code Jam problems.
	for idx in xrange(0,testCases):
		n = input() # this is the random number N
		match = False 
		i = 1
		numsSeen = []
		while (not match):
			# before calculating anything new, check if the numsSeen array has all the digits we need
			count = 0
			for x in xrange(0,10):
				if (str(x)) in numsSeen:
					count += 1
			if count==10:
				print ("Case #"+(str(idx+1))+": "+temp)
				match = True
				break
			elif i>=2000000:
				print ("Case #"+(str(idx+1))+": INSOMNIA")
				match = True
				break
			temp = i*n
			# print temp
			temp = str(temp)
			for x in xrange(0,len(temp)):
				# print temp[x]
				# this if condition looks un necessary. how about push all the numbers as it is?
				if (temp[x] not in numsSeen):
					numsSeen.append(temp[x])
			# print i
			i += 1



if __name__ == '__main__':
	main()			