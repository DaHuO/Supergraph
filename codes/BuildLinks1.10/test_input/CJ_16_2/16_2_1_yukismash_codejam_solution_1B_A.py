import sys

def lists_same(a, b):
	return sorted(a) == sorted(b)

def main():
	num_test_cases = int(sys.stdin.readline())
	for i in range(num_test_cases):
		input_ = str(sys.stdin.readline().strip())
		print("Case #{}: {}".format(i + 1, function(input_)))

def string_contains(needle, haystack):
	haystack = list(haystack)
	for n in needle:
		if n in haystack:
			haystack.remove(n)
		else:
			return False
	return True

def function(string):
	buckets = [0] * 10
	nums = [('ZERO'), ('ONE'), ('TWO'),
			('THREE'), ('FOUR'), ('FIVE'),
			('SIX'), ('SEVEN'), ('EIGHT'),
			('NINE')]
	order = [0, 2, 4, 6, 8, 5, 7, 1, 9, 3]
	for i in order:
		while string_contains(nums[i], string):
			buckets[i] += 1
			string = list(string)
			for char in nums[i]:
				string.remove(char)
			string = ''.join(string)
	if string != "":
		print("WTF FUUUUUUUCK")
	return ''.join([str(i) * buckets[i] for i in range(len(buckets))])

if __name__ == '__main__':
	main()