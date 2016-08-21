
def update_set(s, n):
	'''
	@param n the number named
	@param s the set maintained to be the digits that has been seen
	@effect s is updated
	@return if 0~9 has all been seen after seeing n
	'''
	s |= set(list(str(n)))
	return len(s)==10


def time(n):
	'''
	@param n the starting number
	@return the last number to name 
	'''
	if n == 0: return 'INSOMNIA'
	digits = set()
	count = 1
	temp = n*count
	while not update_set(digits,temp):
		temp += n
		count += 1
	return temp

def solve(filename, file_out):
	'''
	@param filename the path to the input file
	@param file_out the path to the output file
	'''
	f = open(filename)
	fout = open(file_out,'w')
	num_problems = int(f.readline())
	for i in xrange(num_problems):
		answer = str(time(int(f.readline())))
		fout.write( 'Case #'+str(i+1)+': '+answer+'\n' )
	f.close()
	fout.close()

solve('A-large.in.txt', 'output_a.txt')

