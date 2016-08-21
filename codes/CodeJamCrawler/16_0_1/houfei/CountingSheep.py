def counting_sheep(number):
	base=set(['0','1','2','3','4','5','6','7','8','9'])
	compare=set()
	for i in range(100):
		result=str(int(number)*(i+1))
		for digit in result:
			if digit not in compare:
				compare.add(digit)
				if compare==base:
					return result
	else:
		return 'INSOMNIA'

if __name__ == "__main__":
	fopen=open('test.in')
	output=open('output.txt', 'a')
	line_number=0
	for lines in fopen:
		if(line_number==0):
			line_number=line_number+1
			continue
		number=lines.strip()
		output.write('Case #'+str(line_number)+': ')
		output.write(counting_sheep(number)+'\n')
		line_number = line_number + 1
	output.close()