CASE = 'Case #{}: '

def min_flips(pancakes):
	pancakes = list(pancakes)
	flips = 0
	n = len(pancakes)
	
	face_up = 0
	i = -1
	while i >= -n and pancakes[i] == '+':
		face_up += 1
		i -= 1

	face_down = 0
	while face_up < n:
		pancake_stack = pancakes[:n-face_up]
		for c in pancake_stack:
			if c == '-':
				face_down += 1
			else:
				if face_down == 0:
					k = 0
					j = 0
					len_p_s = len(pancake_stack)
					while k < len_p_s and pancake_stack[k] == '+':
						k += 1
					while k + j < len_p_s and pancake_stack[k+j] == '-':
						j += 1
					pancakes[:k] = ['-'] * k
					if pancakes[:len_p_s] == ['-'] * len_p_s:
						return flips + 2
					face_down = k + j
					flips += 1
				break
		pancakes[0:n-face_up] = map(lambda x: '-' if x == '+' else '+', pancake_stack[::-1])
		pancakes = pancakes
		face_up += face_down
		face_down = 0
		flips += 1
	return flips


T = int(raw_input())
for i in xrange(T):
	pancakes = raw_input()
	print CASE.format(i + 1), min_flips(pancakes)

