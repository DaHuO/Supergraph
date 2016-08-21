file = open('A-large.txt')

lines = file.readlines()

i = 1

n2sheep = open('n2sheep.txt','w')

testcases = lines[0]
testcases = int(testcases)

while i <= testcases:
	n = int(lines[i])
	
	answer = '...'
	
	if n == 0:
		answer = 'INSOMNIA'
	else:
		digits = [0,0,0,0,0,0,0,0,0,0]
		k = 2
		norig = n
		while True:
			
			
			ns = str(n)
		
			x = 0
			while x < len(ns):
				if ns[x] == '0':
					digits[0] = 1
				elif ns[x] == '1':
					digits[1] = 1
				elif ns[x] == '2':
					digits[2] = 1
				elif ns[x] == '3':
					digits[3] = 1
				elif ns[x] == '4':
					digits[4] = 1
				elif ns[x] == '5':
					digits[5] = 1
				elif ns[x] == '6':
					digits[6] = 1
				elif ns[x] == '7':
					digits[7] = 1
				elif ns[x] == '8':
					digits[8] = 1
				elif ns[x] == '9':
					digits[9] = 1
				x = x + 1
		
		
			if digits == [1,1,1,1,1,1,1,1,1,1]:
			#n is the number
				answer = str(n)
				break
			else:
				n = n + norig
				k = k + 1
				if k > 1000000:
					answer = 'INSOMNIA'
					break
	
	line = 'Case #' + str(i) + ': ' + str(answer) + '\n'
	
	n2sheep.write(line)

	i = i + 1
	
n2sheep.close()
file.close()