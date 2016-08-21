import sys

# Import the file as a list of lines:
size = sys.argv[1]

path = '/Users/mikevanderheyden/GitHub/codejam/2016/Qual/'
fin = path + 'B-' + size + '.in.txt'
fout = path + 'B-' + size + '.out.txt'

with open(fin,'rb') as f:
	lines = f.read().splitlines()

num_cases = int(lines[0])

with open(fout,'wb') as f:
	for i in xrange(1,len(lines)):
		s = list(lines[i])
		sr = s[::-1]
		for l in sr:
			if l == '+':
				s.pop()
			else:
				break
		print s
		lastchar = 'x'
		flipcount = 0
		for l in s:
			if l != lastchar:
				flipcount += 1
			lastchar = l
		f.write('Case #' + str(i) + ': ' + str(flipcount) + '\n')
		