import sys

def process(fin):
	startingNum = int(fin.readline())
	missing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	currNum = startingNum
	while(True):
		temp = currNum
		while(temp > 0):
			digit = temp % 10
			if digit in missing:
				missing.remove(digit)
			temp = int(temp / 10)
		if len(missing) == 0:
			return currNum
		currNum = currNum + startingNum
		if currNum == startingNum:
			return -1


def main():
	input_name = sys.argv[1]
	fin = open(input_name, 'r')

	num_cases = int (fin.readline())
	for i in range(num_cases):
		result = process(fin)
		if result == -1:
			print("Case #{}: INSOMNIA".format((i+1), result))
		else:
			print("Case #{}: {}".format((i+1), result))

if __name__== '__main__':
	main()