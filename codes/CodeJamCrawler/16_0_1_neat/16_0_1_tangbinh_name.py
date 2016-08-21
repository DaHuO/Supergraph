import sys

def last_number(number):
	if number == 0:
		return 'INSOMNIA'
	s = [str(i) for i in xrange(10)]
	for i in xrange(1, 1000):		
		new = str(number * i)
		for ch in new:
			if ch in s:
				s.remove(ch)
		if len(s) == 0:
			return new

def main(filename):
	file = open(filename)
	T = int(file.readline())
	ans = ''
	for i in xrange(1, T + 1):
		ans += 'Case #' + str(i) + ': ' + last_number(int(file.readline())) + '\n'
	output = open('/Users/btang/Downloads/output.txt', 'w')
	output.write(ans)

if __name__ == '__main__':
	main(sys.argv[1])