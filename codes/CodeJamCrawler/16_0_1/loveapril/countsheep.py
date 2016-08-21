def countsheep(num):
	dtb_number = [i for i in xrange(10)]
	mul = 1
	if num==0:
		return 'INSOMNIA'
	while 1:
		n = mul*num
		digits = [int(i) for i in str(n)]
		while len(digits)>0:
			d = digits.pop()
			if d in dtb_number:
				dtb_number.remove(d)
				if len(dtb_number)==0:
					return n
		mul += 1

def main():
	filename = 'A-large.in'
	output = 'A-large.out'
	f = open(filename,'r')
	#Output file
	out = open(output,'w')
	while True:
		line = f.readline()
		if line == '':
			break
		num_tests = int(line)
		for i in xrange(num_tests):
			line = f.readline()
			num = countsheep(int(line))
			s = 'Case #%s: ' %(i+1)
			s = s + str(num)
			out.write(s)
			out.write('\n')
		
if __name__ == "__main__":
	main()