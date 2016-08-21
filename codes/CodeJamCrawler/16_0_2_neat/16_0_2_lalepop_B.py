def algo(line):
	ret = 0
	prev_char = line[0]
	if prev_char == '+':
		ret += 1
	clean_line = line.strip()
	a = []
	a.append(prev_char)
	for pancacke in clean_line:
		if prev_char != pancacke and prev_char == '-':
			a.append(pancacke)
			ret += 1
		if prev_char != pancacke and prev_char == '+':
			ret += 2
			a.append(pancacke)
		prev_char = pancacke
	#print(a)
	if a[0] == '-':
		return len(a) - (len(a)+1)%2
	else:
		return len(a) - (len(a))%2
	#return str(ret-1)
		
	


if __name__ == '__main__':
	
	fout = open('B-large.out', 'w')

	with open('B-large.in','r') as fin:
		number_of_cases = fin.readline()

		case = 1
		for line in fin.readlines():
			#print(line)
			ans = algo(line)
			fout.write("Case #{0}: {1}\n".format(str(case), ans))
			case += 1
