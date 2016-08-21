filename = ('A-large.in')

from collections import Counter
from collections import defaultdict

def solve(w):
	letters = list(w)
	l = list()
	while 'Z' in letters:
		p = letters.index('Z')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		p = letters.index('R')
		del(letters[p])
		p = letters.index('O')
		del(letters[p])
		l.append(0)
	while 'X' in letters:
		p = letters.index('S')
		del(letters[p])
		p = letters.index('I')
		del(letters[p])
		p = letters.index('X')
		del(letters[p])
		l.append(6)
	
	while 'W' in letters:
		p = letters.index('T')
		del(letters[p])
		p = letters.index('W')
		del(letters[p])
		p = letters.index('O')
		del(letters[p])
		l.append(2)

	while 'U' in letters:
		p = letters.index('F')
		del(letters[p])
		p = letters.index('O')
		del(letters[p])
		p = letters.index('U')
		del(letters[p])
		p = letters.index('R')
		del(letters[p])
		l.append(4)
	
	while 'S' in letters:
		p = letters.index('S')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		p = letters.index('V')
		del(letters[p])
		p = letters.index('N')
		del(letters[p])
		l.append(7)

	while 'G' in letters:
		p = letters.index('E')
		del(letters[p])
		p = letters.index('I')
		del(letters[p])
		p = letters.index('G')
		del(letters[p])
		p = letters.index('H')
		del(letters[p])
		p = letters.index('T')
		del(letters[p])
		l.append(8)
	while 'O' in letters:
		p = letters.index('O')
		del(letters[p])
		p = letters.index('N')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		l.append(1)
	while 'N' in letters:
		p = letters.index('N')
		del(letters[p])
		p = letters.index('I')
		del(letters[p])
		p = letters.index('N')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		l.append(9)

	while 'T' in letters:
		p = letters.index('T')
		del(letters[p])
		p = letters.index('H')
		del(letters[p])
		p = letters.index('R')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		l.append(3)
	
	while 'V' in letters:
		p = letters.index('F')
		del(letters[p])
		p = letters.index('I')
		del(letters[p])
		p = letters.index('V')
		del(letters[p])
		p = letters.index('E')
		del(letters[p])
		l.append(5)

	l = sorted(l)
	k = [str(elem) for elem in l]
	return "".join(k)
	


with open(filename, 'r') as f, open('out1.txt', 'w') as f2:
	f.readline()
	case = 1
	for line in f:
		w = line.strip()
		ans = solve(w)
		f2.write('Case #{0}: {1}\n'.format(case, ans))
		case += 1