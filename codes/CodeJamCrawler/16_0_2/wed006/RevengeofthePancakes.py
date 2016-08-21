def main():
	file = open("/Users/daviddai/Desktop/in.txt", "r")
	data = file.read()
	file.close()

	data = data.split()[1:]
	opt = ''

	for i, j in enumerate(data):
		opt += "Case #" + str(i + 1) + ": " + str(solve(j)) + "\n"

	file = open('result.txt', 'w')
	file.write(opt)
	file.close()

def solve(cakes):
	if not cakes:
		return 0
	if len(cakes) == 1:
		if cakes == '-':	return 1
		return 0
		
	#last -   flip to ---- then +1
	if cakes[-1] == '-':
		rev = ''
		for i in cakes:
			if i == '+':
				rev += '-'
			else:
				rev += '+'
		return 1 + solve(rev)
	#last+ flip to ++++
	else:
		return solve(cakes[:len(cakes) - 1])



main()



