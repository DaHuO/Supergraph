def flips(stack):
	stack = stack[::-1]
	if(stack[0]) == "-":
		count = 1
	else:
		count = 0
	prev_char = stack[0]
	for char in stack[1:]:
		if(char != prev_char):
			prev_char = char
			count += 1
	return count

f = open('B-large.in.txt', 'r')
f2 = open('outputLarge.txt', 'w')
final = ''

for i in range(1, int(f.readline().strip())+1):
	s = f.readline().strip()
	final += 'Case #{}: {}\n'.format(i, flips(s))

f2.write(final)