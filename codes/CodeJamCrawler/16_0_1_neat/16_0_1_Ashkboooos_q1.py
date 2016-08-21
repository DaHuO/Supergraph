def main():
	file_name = 'A-large.in'
	f = open(file_name , 'r')
	lines = f.read().splitlines()
	test_cases = int(lines[0])
	result = ''
	for i in xrange(1, test_cases + 1):
		line = lines[i].strip()
		n = int(lines[i])
		nn = n
		if n == 0:
			r = "Case #" + str(i) + ": " + 'INSOMNIA' + '\n'
		else:
			digits = list(set([a for a in line]))
			flag = False
			y = 1
			if len(digits) == 10:
				flag = True
			while not flag:
				y += 1
				nn = y * n
				digits.extend([e for e in str(nn)])
				#print n,y, nn, digits
				digits = list(set(digits))
				if len(digits) == 10:
					flag = True
			r = "Case #" + str(i) + ": " + str(nn) + '\n'
		result += r
	print result
	#print max_y
	f = open('q1.out', 'w')
	f.write(result)
	f.close()
if __name__ == '__main__':
	main()
