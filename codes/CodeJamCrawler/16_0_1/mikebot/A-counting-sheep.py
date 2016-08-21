import sys

# Import the file as a list of lines:
size = sys.argv[1]

path = '/Users/mikevanderheyden/GitHub/codejam/2016/Qual/'
fin = path + 'A-' + size + '.in.txt'
fout = path + 'A-' + size + '-practice.out.txt'

with open(fin,'rb') as f:
	lines = f.read().splitlines()

num_cases = int(lines[0])

with open(fout,'wb') as f:
	for i in xrange(1,len(lines)):
		digits_found = []
		found = 0
		#x = lines[i].split()
		n = int(lines[i])
		print 'NEW CASE'
		print n
		for j in xrange(1,1000):
			cur_n = j * n
			#print cur_n
			curdigs = list(str(cur_n))
			digits_found += curdigs
			if len(set(digits_found)) == 10:
				found = 1
				break
		if found == 1:
			f.write('Case #' + str(i) + ': ' + str(cur_n) + '\n')
			print 'CASE DONE - FOUND' + str(cur_n) 
		else:
			f.write('Case #' + str(i) + ': INSOMNIA\n')
			print 'CASE DONE - NOT FOUND'
		






