import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		N = int(sys.stdin.readline())
		all = 2*N-1
		il = []
		
		while all != 0:
			all -= 1
			input = sys.stdin.readline()
			input = input.strip()
			input = list(map(int, (input.split(' '))))
			
			il.append(input)
		
		line = []
		
		for i in range(0, N):
			l = []
				
			il.sort(key = lambda x : x[i])
			
			l.append(il[i*2])
			
			if i < N - 1 and il[i*2][i] == il[i*2+1][i]:
				l.append(il[i*2+1])
			
			if i > 0 and il[i*2][i] == il[i*2-1][i]:
				l.append(il[i*2-1])
				
			line.append(l)
			
			if len(l) == 1:
				index = i
			
		
		answer = []
		for i in range(0, N):
			if i == index:
				answer.append(str(line[i][0][index]))
				continue
				
			if line[i][0][index] == line[index][0][i]:
				answer.append(str(line[i][1][index]))
			else:
				answer.append(str(line[i][0][index]))
			
		

		output = 'Case #{0}: {1}'.format(cases, ' '.join(answer))
		print(output)
		cases += 1

