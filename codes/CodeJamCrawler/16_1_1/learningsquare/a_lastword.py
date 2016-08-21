def solve_case(given_string):
	answer = given_string[0]
	for char in given_string[1:]:
		if ord(char) >= ord(answer[0]):
			answer = char + answer
		else:
			answer = answer + char

	return answer