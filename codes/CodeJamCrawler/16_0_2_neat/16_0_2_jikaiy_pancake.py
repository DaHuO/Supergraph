
def pancake( cake ):
	res = ''
	prev = cake[0]
	for i in range(1, len(cake)):
		if cake[i] != prev:
			res += prev
			prev = cake[i]
	res += prev
	return res

def flip_cake( cake ):
	if cake == '+':
		return 0
	if cake == '-':
		return 1
	if cake == '+-':
		return 2
	if cake == '-+':
		return 1
	return 1 + flip_cake(cake[1:])

def get_flip(cake):
	cake = pancake(cake)
	return flip_cake(cake)

if __name__ == '__main__':
	t = int(raw_input())
	for i in xrange(1, t+1):
		cake = str(raw_input())
		print "Case #{}: {}".format(i, get_flip(cake))