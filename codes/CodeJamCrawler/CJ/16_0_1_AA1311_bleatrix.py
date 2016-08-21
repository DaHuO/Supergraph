import sys
import os

def input(inputfile):
	"""
	Returns a dictionary
	"""
	f = open(inputfile)
	T = f.readline()
	JC = []
	try:
		for i in range(int(T)):
			NJ = f.readline()
			NJ = int(NJ)
			JC.append(NJ)
		f.close()
		return JC
	except Exception:
		return False

def output(result, filename):
	f = open(filename, 'w')
	count = 1
	for i in range(len(result)):
		# each i is a test case result
		case = "Case #" + str(i+1) + ': ' + str(result[i]) + '\n'
		f.write(case)
	f.close()


def main():
	"""
	result = [[J, list2], [J, list2], ...]

	"""
	
	# l = permute(16)
	# print l

	
	T = input(sys.argv[1])
	# print T
	
	result = []
	for i in range(len(T)):
		lastnum = bleatrix_sleep(T[i])
		result.append(lastnum)


	# print result
	output(result, sys.argv[2])
	
def bleatrix_sleep(n):
	# if(n == 0 or n == 1):
	# 	return 'INSOMNIA'
	h = set()
	i = 1
	while(True):
		next = i * n
		next = str(next)
		# hash every digit
		for j in range(1, len(next)+1):
			h.add(int(next[j-1]))
		if(len(h) == 10):
			# print i
			return int(next)
		else:
			i += 1
			if(i == 1000000):
				return 'INSOMNIA'
			else:
				continue


main()
