import sys

#count = 0 
input = []
def process_file(fileName):
	input_file = open(fileName, "r")
	first = True
	for line in input_file:
		line = line.strip()
#		if first == True: 
#			count = line 
#			first = False 
#		else: 
		input.append(line)
	input_file.close()

allDigits = set([0,1,2,3,4,5,6,7,8,9])

def isAllDigits(s):
	if ((allDigits - s) == set([])): 
		return True
	else: 
		return False

def makeDigits(num):
	s2 = set() 
	count = 1
	result = -1

	while True:
		res = count * num 
		temp = res 
		count += 1
		if res == 0: 
			break 
		if count == 1000:
			break
		while res: 
			s2.add(res % 10) 
			res = int(res / 10) 
		if isAllDigits(s2):
			result = temp  
			break
	return result 		


def process_sol():
	count = int(input.pop(0))

	cnt = 0
	for i in input:
#		print("Case #" + str(cnt) +": ", end='')
		cnt += 1
		res = makeDigits(int(i))
		if res == -1 : 
			print("Case #" + str(cnt) +": " +"INSOMNIA")
		else: 
			print("Case #" + str(cnt) +": " +str(res))

if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = process_file(fn)
	process_sol() 