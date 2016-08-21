import string
def max_index(nums):
	index = 0
	for i in range(len(nums)):
		if nums[i] > nums[index]:
			index = i
	return index

def to_alpha(i):
	return string.ascii_uppercase[i]

def compute(N,nums):
	result = ''
	count = sum(nums)
	while count>3:
		i1 = max_index(nums)
		nums[i1] -= 1
		i2 = max_index(nums)
		nums[i2] -= 1
		result += ' ' + to_alpha(i1) + to_alpha(i2)
		count -= 2
	if count == 3:
		i1 = max_index(nums)
		nums[i1] -= 1
		result += ' ' + to_alpha(i1)
		count -= 1
		
		i1 = max_index(nums)
		nums[i1] -= 1
		i2 = max_index(nums)
		nums[i2] -= 1
		result += ' ' + to_alpha(i1) + to_alpha(i2)
		count -= 2
	if count == 2:
		i1 = max_index(nums)
		nums[i1] -= 1
		i2 = max_index(nums)
		nums[i2] -= 1
		result += ' ' + to_alpha(i1) + to_alpha(i2)
		count -= 2
	return result

if __name__ == '__main__':
	input = open('input.txt','r')
	output = open('output.txt','w')

	T = int(input.readline())
	for i in range(1,T+1):
		N = input.readline()
		nums = [int(j) for j in input.readline().split()]
		result = compute(N,nums)
		output.write('Case #{}: {}\n'.format(i,result))
	

