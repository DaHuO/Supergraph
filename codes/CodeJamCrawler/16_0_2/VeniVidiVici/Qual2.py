def check(arr):
	for i in range(len(arr)):
		if arr[i] is 0:
			return False
	return True

def flip(arr):
	start = 0
	end = len(arr) - 1
	if arr[0] is 1:
		while arr[start] is 1:
			arr[start] = 0
			start = start + 1
		return arr
	while arr[end] is 1:
		end = end - 1
	start = 0
	while end >= start:
		arr[start], arr[end] = arr[end], arr[start]
		if start == end:
			arr[start] = 1 - arr[start]
		else:
			arr[start] = 1 - arr[start]
			arr[end] = 1 - arr[end]
		start = start + 1
		end = end - 1
	return arr

def testcase(arr):
	num_flips = 0
	while check(arr) is False:
		arr = flip(arr)
		num_flips = num_flips + 1
	return num_flips
	
def conv(s):
	ret = []
	for i in range(len(s)):
		if s[i] is '+':
			ret.append(1)
		elif s[i] is '-':
			ret.append(0)
	return ret
	
input = open('B-large.in', 'r')
output = open('B-large-output', 'w')
T = int(input.readline())

for i in range(T):
	inp = input.readline()
	inp = conv(inp)
	print(inp)
	out = 'Case #' + str(i + 1) + ': ' + str(testcase(inp)) + '\n'
	output.write(out)
	print(out)
	