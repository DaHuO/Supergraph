import sys

def remove0(numbers):
	numbers.remove('Z');
	numbers.remove('E');
	numbers.remove('R');
	numbers.remove('O');

def remove1(numbers):
	numbers.remove('O');
	numbers.remove('N');
	numbers.remove('E');

def remove2(numbers):
	numbers.remove('T');
	numbers.remove('W');
	numbers.remove('O');

def remove3(numbers):
	numbers.remove('T');
	numbers.remove('H');
	numbers.remove('R');
	numbers.remove('E');
	numbers.remove('E');

def remove4(numbers):
	numbers.remove('F');
	numbers.remove('O');
	numbers.remove('U');
	numbers.remove('R');

def remove5(numbers):
	numbers.remove('F');
	numbers.remove('I');
	numbers.remove('V');
	numbers.remove('E');

def remove6(numbers):
	numbers.remove('S');
	numbers.remove('I');
	numbers.remove('X');

def remove7(numbers):
	numbers.remove('S');
	numbers.remove('E');
	numbers.remove('V');
	numbers.remove('E');
	numbers.remove('N');

def remove8(numbers):
	numbers.remove('E');
	numbers.remove('I');
	numbers.remove('G');
	numbers.remove('H');
	numbers.remove('T');

def remove9(numbers):
	numbers.remove('N');
	numbers.remove('I');
	numbers.remove('N');
	numbers.remove('E');


def process(fin):
	nums = list(fin.readline().strip())
	result = []
	while(nums):
		if 'Z' in nums:
			result.append(0)
			remove0(nums)
		elif 'W' in nums:
			result.append(2)
			remove2(nums)
		elif 'X' in nums:
			result.append(6)
			remove6(nums)
		elif 'G' in nums:
			result.append(8)
			remove8(nums)
		elif 'H' in nums:
			result.append(3)
			remove3(nums)
		elif 'S' in nums:
			result.append(7)
			remove7(nums)
		elif 'V' in nums:
			result.append(5)
			remove5(nums)
		elif 'U' in nums:
			result.append(4)
			remove4(nums)
		elif 'I' in nums:
			result.append(9)
			remove9(nums)
		elif 'O' in nums:
			result.append(1)
			remove1(nums)
	result.sort()
	return result

def main():
    input_name = sys.argv[1]
    fin = open(input_name, 'r')

    num_cases = int (fin.readline())
    for i in range(num_cases):
        result = process(fin)
        print("Case #{}: {}".format((i+1), ''.join(map(str, result))))

if __name__ == '__main__':
    main()