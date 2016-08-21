import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

T = lines[0]

for case in range(1,int(T)+1):
	i = 1
	N = int(lines[case])
	digit = [0,0,0,0,0,0,0,0,0,0]
	memory = {}
	while True:
		#print ('MEMORY:' + str(memory))
		if memory.get(int(i * N), None) == None:
			memory[int(i * N)] = 1
		else:
			y = 'INSOMNIA'
			break
		#print ('MEMORY:' + str(memory))
		
		#print('DIGIT:' + str(digit))
		val = list(str(i * N))
		for c in val:
			digit[int(c)] = int(1)
			
		#print('DIGIT:' + str(digit))
		count = 0
		for d in digit:
			count = count + d
			
		#print('COUNT' + str(count))
		if count == 10:
			y = i * N
			break
		else:
			i = i + 1
		
		#sys.stdin.read(1)
			
	print('Case #' + str(case) + ': ' + str(y))