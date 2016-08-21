

def count_sheep( input_ ):
	if input_ == 0:
		return "INSOMNIA"
	digit = set()
	x = input_
	while True:
		x_string = str(x)
		for c in x_string:
			digit.add(c)
		if len(digit) == 10:
			return x
		x += input_ 

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange( 1, t+1 ):
		n = int(raw_input())
		print "Case #{}: {}".format(i, count_sheep(n))



