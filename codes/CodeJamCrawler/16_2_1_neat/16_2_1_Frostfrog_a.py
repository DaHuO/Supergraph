import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	digits = list(map(str, range(0, 10)))
	while T != 0: 
		T -= 1
		input = sys.stdin.readline()
		input = input.strip()
		
		test = 'ZOWTUVXSGE'
		l = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
		ord = [0, 2, 4, 6, 8, 3, 7, 1, 5, 9]
		ans = []
		while len(input) > 0:
			for i in ord:
				while len(input) > 0 and test[i] in input:
					ans.append(str(i))
					#print(i)
					#print(input)
					for k in l[i]:
						input = input.replace(k, '', 1)
					
					
		ans.sort()
		
		output = 'Case #{0}: {1}'.format(cases, ''.join(ans))
		print(output)
		cases += 1