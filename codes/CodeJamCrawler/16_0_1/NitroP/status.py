import math

def num_l(num):
	return int(math.log(num) / math.log(10) + 1 + 1e-7)

def solve(num):
	d = set()
	c = 1
	while(len(d) < 10):
		a = 1
		temp = num * c
		for i in range( num_l(temp) ):
			d.add( int(temp / a) % 10 )
			a *= 10
		c += 1 
	return num*(c-1)

if __name__ == '__main__':
	f = open('test.txt')
	o = open('output.txt', 'w')
	for index, line in enumerate(f.readlines()[1:]):
		num = int(line)
		if num == 0:
			o.write("Case #%d: INSOMNIA\n" % (index + 1))
		else:
			o.write("Case #%d: %d\n" % (index + 1, solve(num)))
