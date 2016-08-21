
def getBleatrix(n) :
	if int(n) == 0 :
		return "INSOMNIA"

	digit = set()

	cnt = 1
	l = n

	while len(digit) < 10 :
		for i in l :
			digit.add( int(i) )

		if len(digit) == 10 :
			break

		cnt = cnt + 1;
		l = str(int(n) * cnt)

	return str(l);



results = []
with open('A-large.in') as f :
	line = f.read().splitlines()

	num = line[0]

	for i in range(1, int(num)+1) :
		r = getBleatrix( line[i] )
		results.append(r)


with open('countingsheep_result.out', 'w') as f :
	for i in range(0,len(results)) :
		f.write('Case #' + str(i+1) + ': ' + str(results[i]) + '\n')















