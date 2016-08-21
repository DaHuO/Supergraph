t = int(input())
case = 0

while t:
	t -= 1
	case += 1
	n = []
	s = input()
	s = [c for c in s]
	while len(s) != 0:
		if 'Z' in s:
			n.append(0)
			for i in 'ZERO':
				s.remove(i)
		if 'W' in s:
			n.append(2)
			for i in 'TWO':
				s.remove(i)
		if 'X' in s:
			n.append(6)
			for i in 'SIX':
				s.remove(i)
		if 'G' in s:
			n.append(8)
			for i in 'EIGHT':
				s.remove(i)
		if 'U' in s:
			n.append(4)
			for i in 'FOUR':
				s.remove(i)
		if 'T' in s and 'H' in s and 'R' in s and s.count('E') >= 2:
			n.append(3)
			for i in 'THREE':
				s.remove(i)
		if 'F' in s and 'I' in s and 'V' in s and 'E' in s:
			n.append(5)
			for i in 'FIVE':
				s.remove(i)
		if 'S' in s and 'V' in s and 'N' in s and s.count('E') >= 2:
			n.append(7)
			for i in 'SEVEN':
				s.remove(i)	
		if 'O' in s and 'N' in s and 'E' in s:
			n.append(1)
			for i in 'ONE':
				s.remove(i)
		if 'I' in s and 'E' in s and s.count('N') >= 2:
			n.append(9)
			for i in 'NINE':
				s.remove(i)
		#print(''.join(s), n)
	n.sort()
	n = [str(d) for d in n]
	n = ''.join(n)

	print('Case #', case, ':', sep='', end = ' ')
	print(n)