import sys
from itertools import izip

# f = sys.stdin
f = open('A-large.in')
o = open('testou3t.out', 'w')

if __name__ == "__main__":
	total = f.readline()
	
	for i in range(int(total)):
		line = f.readline()
		to_find = set(map(str, range(10)))
		start = int(line)
		ans = str(start)
		j = 1

		if ans != '0':

			while True:
				found = set()
			
				for s in to_find:
					if s in ans:
						found.add(s)

				to_find -= found
			
				if not len(to_find):
					break
			
				else:
					j += 1
					ans = str(j * start)


			o.write('Case #%s: %s\n' % (i + 1, ans))
		else:
			o.write('Case #%s: INSOMNIA\n' % (i + 1))