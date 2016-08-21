from Queue import Queue

def is_done(s):
	return s.find('-') == -1


def greedy(input_string):
	action_count = 0
	if is_done(input_string):
		return action_count

	if input_string[0] == '-':
		input_string = flip_string(input_string)
		action_count += 1
		if is_done(input_string):
			return action_count
		input_string = tail_process(input_string)
	else:
		input_string = head_process(input_string)
		action_count += 1

	action_count += greedy(input_string)
	return action_count


def flip_string(string):
	"""Reverse the string, and flip +/- of it"""
	string = string[::-1]
	new_string = ''

	for char in string:
		if char == '-':
			new_string += '+'
		else:
			new_string += '-'
	return new_string


def head_process(string):
	"""flip all heading ++++s into ----s"""
	l_index = 0
	new_head = ''
	while l_index < len(string) and (string[l_index] == '+'):
		new_head += '-'
		l_index += 1
	return new_head + string[l_index:]


def tail_process(string):
	"""removes the tailing +++s"""
	r_index = len(string)
	while string[r_index - 1] == '+':
		r_index -= 1
	return string[:r_index]


if __name__ == '__main__':
	with open('B-large.in', 'r') as input, open('B-large.out', 'w') as output:
		T = int(input.readline())
		for i in xrange(T):
			s = input.readline().strip()
			if is_done(s):
				action_count = 0
			else:
				action_count = greedy(tail_process(s))
			output.write('Case #{case_number}: {output}\n'.format(
					case_number=i + 1,
					output=action_count,
				)
			)
