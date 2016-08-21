#!/usr/bin/python3

digits = (
	('Z', 'ZERO', 0),
	('W', 'TWO', 2),
	('U', 'FOUR', 4),
	('O', 'ONE', 1),
	('R', 'THREE', 3),
	('F', 'FIVE', 5),
	('X', 'SIX', 6),
	('S', 'SEVEN', 7),
	('G', 'EIGHT', 8),
	('I', 'NINE', 9)
)

t = int(input())
for icase in range(1, t+1):
	word = list(input().strip())
	ds = []
	for l, cs, d in digits:
		if l in word:
			n = word.count(l)
			ds += n * [d]
			for c in cs:
				for i in range(n):
					word.remove(c)
	nr = ''.join(map(str, sorted(ds)))
	print('Case #%d: %s' % (icase, nr))
