import sys

# WARNING: Assumes all input is squeaky clean.

def main():
	T = int(sys.stdin.readline())

	for case_num in range(1,T+1):
		S = sys.stdin.readline()
		number_of_flips = 0
		while not all_pluses(S):
			# find where the last '-' is
			last_minus_location = S.rfind('-')+1
			# find where the top group of '+' ends
			num_top_pluses = S.find('-')
			if num_top_pluses > 0:
				S = flip_top_i(S, num_top_pluses)
				number_of_flips += 1
			S = flip_top_i(S, last_minus_location)
			number_of_flips += 1
			
		print("Case #{0}: {1}").format(case_num, number_of_flips)

def flip_top_i(S, i):
	S_list = list(S)
	first = S_list[:i]
	first = ['+' if c == '-' else '-' for c in first][::-1]
	rest = S_list[i:]
	new_stack = ''.join(first+rest)
	return new_stack

def all_pluses(S):
	return S.find('-') == -1

if __name__ == "__main__":
	main()