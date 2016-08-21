# Samantha Spano
# Counting Sheep



def largestNum(n):
	count = [0]*10
	if (n == 0):
		return "INSOMNIA"

	i = 0
	while (sum(count)<10):
		#print count
		i += 1
		ntimes = i * n
		nstr = str(ntimes)
		nstr = "".join(set(nstr))  # remove dups

		for num in nstr:
			if (count[int(num)] == 0):
				count[int(num)] = 1
	return ntimes

def writeToFile(filename, nums):
	str1 = "Case #"
	str2 = ": "
	file = open(filename, 'w')
	file.seek(0)
	for n in range(len(nums)):
		caseStr = str1 + str(n+1) + str2 + str(nums[n]) + "\n"
		file.write(caseStr)
	file.close()

def printCases(nums):
	str1 = "Case #"
	str2 = ": "
	for n in range(len(nums)):
		print str1 + str(n+1) + str2 + str(nums[n]) 

def countingSheep(filename):
	file = open(filename, 'r')
	import pdb

	content = file.read().splitlines()
	#pdb.set_trace()
	numLines = int(content[0])
	ints = content[1:]
	nums = [0]*numLines
	for i in range(int(numLines)):
		nums[i] = largestNum(int(ints[i]))
	file.close()
	writeToFile(filename, nums)
	printCases(nums)
	

countingSheep("A-large.in")


