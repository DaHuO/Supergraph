import sys


def fliplist(l, index):
	l[0:index] = list(map(lambda x: not x, l[0:index][::-1]))
	

if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		input = sys.stdin.readline()
		
		bitinput = []
		
		for i in input:
			if i == '-':
				bitinput.append(False)
			
			if i == '+':
				bitinput.append(True)

		count = 0
		while False in bitinput:
			if bitinput[0] == True:
				fliplist(bitinput, bitinput.index(False))
			else:
				fliplist(bitinput, len(bitinput) - bitinput[::-1].index(False))
			count += 1
			
		output = 'Case #{0}: {1}'.format(cases, count)
		cases += 1
		print (output)
				
		