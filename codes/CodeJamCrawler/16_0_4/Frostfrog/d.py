import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		input = sys.stdin.readline().split()
		K, C, S = map(int, input[0:3])
		
		if (K + C - 1) / C > S:
			output = 'Case #{0}: {1}'.format(cases, 'IMPOSSIBLE')
			print(output)
			cases += 1
			continue
			
		
		l = range(0, K)
		
		i = 0
		ii = 0
		r = 0
		answer = []
		ll = []
		for i in range(0, K, C):
			ll.append(l[i:i+C])
			
		#print (ll)
		
		for k in ll:
			ii = 0
			for i in k:
				ii = ii * K + i
			
			answer.append(ii+1)
			
		
		answer = list(map(str, answer))
		
		output = 'Case #{0}: {1}'.format(cases, ' '.join(answer))
		print(output)
		cases += 1
