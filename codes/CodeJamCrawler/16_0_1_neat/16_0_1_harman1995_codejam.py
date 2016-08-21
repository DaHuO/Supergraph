from sets import Set

def main():

	N = raw_input()
	N = int(N)
	
	for i in xrange(N):
		s = raw_input()
		s = int(s)
		
		gotdict = Set()
		count = 0
		prod = 0
		while(len(gotdict) < 10 and count < 1000):
			count = count+1
			prod = s*count
			prod = str(prod)
			lissy = list(prod)
			for item in lissy:
				gotdict.add(item)


		if(len(gotdict) == 10):
			print 'Case #' + str(i+1) + ': ' + str(prod)
		else:
			print 'Case #' + str(i+1) + ': INSOMNIA'

if __name__ == '__main__':
	main()