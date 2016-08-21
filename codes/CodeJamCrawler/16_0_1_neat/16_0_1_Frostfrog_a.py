import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		input = int(sys.stdin.readline())
		iter = input
		s = set()
		circle = set()
		while len(s) < 10 and iter not in circle:
			circle.add(iter)
			for each_char in str(iter):
				s.add(each_char)
			
			if len(s) == 10:
				break
				
			iter += input
		
		if len(s) != 10:
			output = 'INSOMNIA'
		else:
			output = str(iter)

		output = 'Case #{0}: {1}'.format(cases, output)
		print(output)
		cases += 1

