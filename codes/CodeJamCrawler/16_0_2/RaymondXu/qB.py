# def pancake(s):
# 	flips = 0
# 	i = len(s) - 1

# 	while i >= 0:
# 		print s
# 		if len(s) >= 2 and s[0] == '+' and s[1] == '-':
# 			s = flip(s, 0)
# 			s = flip(s, 1)
# 			flips += 2
# 		if s[i] == '-':
# 			if s == flip(s, i):
# 				return None
# 			s = flip(s, i)
# 			flips += 1
# 			#i = len(s) - 1
# 		else:
# 			i -= 1

# 	return flips


def pancake(s):
	last = None
	flips = 0

	for char in s:
		if char != last:
			last = char
			flips += 1

	if s[len(s) - 1] == '+':
		flips -= 1

	return flips


# def flip(s, i):
# 	flip_stack = s[0: i + 1]
# 	flip_stack = flip_stack[::-1]
# 	flip_list = list(flip_stack)
	
# 	for j in range(len(flip_list)):
# 		if flip_list[j] == '-':
# 			flip_list[j] = '+'
# 		else:
# 			flip_list[j] = '-'

# 	return ''.join(flip_list) + s[i + 1:]


def main():
	r = open('input_file.txt', 'r')
	w = open('output_file.txt', 'w')

	t = int(r.readline())
	for i in xrange(1, t + 1):
		s = r.readline().strip()
		w.write('Case #{}: {}\n'.format(i, pancake(s)))


main()