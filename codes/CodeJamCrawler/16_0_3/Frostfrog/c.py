import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		input = sys.stdin.readline()
		
		N, J = input.split()[0:2]
		
		print ('Case #1:')
		
		min = (1 << (int(N) - 1)) + 1
		max = 1 << int(N)
		j = int(J)
		
		for i in range(min, max, 2):
			l = []
			x = '{0:b}'.format(i)
			for base in range(2, 11):
				if int(x, base) % (base + 1) != 0:
					break;
				l.append(str(base + 1))
			if len(l) != 9:
				continue
			
			print ('{0} {1}'.format(x, ' '.join(l)))
			j -= 1
			if j  == 0:
				break
		
