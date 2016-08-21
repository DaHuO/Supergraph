
# in --+- -> +-++
def flip( s ) :
	s = s.replace('+', '0')
	s = s.replace('-', '+')
	s = s.replace('0', '-')

	return s[::-1]


# like --+- 
def serve ( s ) :

	cnt = 0

	print s

	while s.rfind('-') >= 0 :
		i = s.rfind('-')

		# ++++++-+++++
		if i == 0 :
			s = flip(s[:i+1]) + s[i+1:]
		elif s[:i].find('-') < 0  :
			s = flip( s[:i] ) + s[i:]
		elif s[0] == '+' :
			r = s[:i].find('-')
			s = flip( s[:r] ) + s[r:]
		else :	
			s = flip( s[:i+1] )  + s[i+1:]
		cnt = cnt + 1


	return cnt



results = []

with open('B-large.in') as f :
	line = f.read().splitlines()

	num = line[0]

	for i in range(1, int(num)+1) :
		r = serve( line[i] )
		results.append(r)


with open('b_result.out', 'w') as f :
	for i in range(0,len(results)) :
		f.write('Case #' + str(i+1) + ': ' + str(results[i]) + '\n')






