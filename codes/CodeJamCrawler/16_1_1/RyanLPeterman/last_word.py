import sys

def main():
	with open(sys.argv[1]) as file_handler:
		test_cases = file_handler.read().splitlines()

		num_cases = test_cases[0]

		for case_num in xrange(int(num_cases)):

			ans = get_last_word(test_cases[case_num+1])

			print "Case #" + str(case_num+1) + ": " + ans 


def get_last_word(string):
	""" Given an input string returns alphabetically last word possible """
	ans = ""

	for char in string:
		if (ans + char) < (char+ ans):
			ans = char + ans
		else:
			ans = ans + char

	return ans

if __name__ == '__main__':
	main()