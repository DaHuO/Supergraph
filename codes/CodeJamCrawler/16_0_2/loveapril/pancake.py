def pancake(cake):
	a = list(cake)
	l = len(a)
	flip_time = 0
	for i in range(l-1,-1,-1):
		if a[i] == '-':
			a = flip(a,i)
			flip_time += 1
	return flip_time
def flip(cake, index):
	a = list(cake)
	l = len(a)
	for i in range(index):
		if a[i]=='+':
			a[i] = '-'
		else:
			a[i] = '+'
	return "".join(a)


def main():
	filename = 'B-large.in'
	output = 'B-large.out'
	f = open(filename,'r')
	#Output file
	out = open(output,'w')
	while True:
		line = f.readline()
		if line == '':
			break
		num_tests = int(line)
		for i in xrange(num_tests):
			line = f.readline().strip()
			num = pancake(line)
			s = 'Case #%s: ' %(i+1)
			s = s + str(num)
			out.write(s)
			out.write('\n')
		
if __name__ == "__main__":
	main()